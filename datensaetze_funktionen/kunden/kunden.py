import datenvorverarbeitung.data_cleaning as dv
import eda.statistiken as st
from eda.visualisierungen import scatterplot, boxplot, histogram
from eda.test import chi_square_test, normality_test
from ml.k_neighbour import knn_classifier, kmeans_cluster_analysis
import pandas as pd

def kunden_main(df):
    """
    Main function to perform analysis on the customer dataset.

    :param df: Input DataFrame containing customer data
    :return: Data Input for output generation
    """
    data = {}
    statistics_texts = []
    data["initial_dataset"] = df.head().to_html(classes="table")

    # Encode Gender to binary
    df_gender = df.copy()
    df = dv.to_binary(df, "Gender", "Male", "Female")
    copy_df = df.copy()
    data["cleaning"] = df.head().to_html(classes="table")

    # Statistical Summary
    summary_stats = []
    for col in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']:
        mean = st.mittelwert(df[col])
        median = st.median(df[col])
        std_dev = df[col].std()
        summary_stats.append({
            "column": col,
            "mean": mean,
            "median": median,
            "std_dev": std_dev
        })
    # Bericht drucken
    for stats in summary_stats:
        col = stats["column"]
        mean = stats["mean"]
        median = stats["median"]
        std_dev = stats["std_dev"]

        if col == "Age":
            distribution_comment = "Das Alter der Kunden ist leicht rechtsschief verteilt (Median < Mittelwert), was darauf hindeutet, dass es mehr jüngere Kunden gibt."
            imagename = "Age"
            histogram(df, col, "Age Distribution", imagename)
        elif col == "Annual Income (k$)":
            distribution_comment = "Die Verteilung des Einkommens ist relativ symmetrisch, da Median und Mittelwert fast gleich sind."
            imagename = "Income"
            histogram(df, col, "Annual Income Distribution", imagename)
        elif col == "Spending Score (1-100)":
            distribution_comment = "Diese Verteilung ist nahezu ausgeglichen, was darauf hinweist, dass die Kunden unterschiedliche Kaufverhalten aufweisen, von sparsamen bis hin zu spendablen Kunden."
            imagename = "Spending"
            histogram(df, col, "Spending Score Distribution", imagename)
        else:
            distribution_comment = "Keine spezifische Verteilungsanalyse verfügbar."

        statistics_texts.append(
            f"<h3>{col}</h3>"
            f"<p>Mittelwert = {mean:.2f}<br>"
            f"Median = {median:.2f}<br>"
            f"Standardabweichung = {std_dev:.2f}<br>"
            f"{distribution_comment}</p>"
            + f'<img src="images/{imagename}.png" alt="{col} Histogram" width="400px" height="400px">'
        )
        # Nach der Schleife alle Texte zusammenfügen
        data["statistics"] = "\n".join(statistics_texts)

    # Correlation and Covariance
    corr_cov_age_income = st.korrelation_kovarianz(df["Age"], df["Annual Income (k$)"])
    data["corr_cov_age_income"] = f"Covariance: {corr_cov_age_income['covariance']:.2f}, Correlation: {corr_cov_age_income['correlation']:.2f}"

    corr_cov_age_spending = st.korrelation_kovarianz(df["Age"], df["Spending Score (1-100)"])
    data["corr_cov_age_spending"] = f"Covariance: {corr_cov_age_spending['covariance']:.2f}, Correlation: {corr_cov_age_spending['correlation']:.2f}"

    corr_cov = st.korrelation_kovarianz(df["Annual Income (k$)"], df["Spending Score (1-100)"])
    data["correlation_covariance"] = f"Covariance: {corr_cov['covariance']:.2f}, Correlation: {corr_cov['correlation']:.2f}"
    scatterplot(df, "Annual Income (k$)", "Spending Score (1-100)", "income_spending")

    # Boxplot: Income by Gender
    boxplot(df_gender, "Gender", "Annual Income (k$)", None, "Annual Income by Gender", "Gender", "Annual Income (k$)", "Boxplot_Income_Gender")

    # Normality Test
    normality_test(df, ['Annual Income (k$)', 'Spending Score (1-100)'])

    # Chi-Square Test
    df['Spending_Category'] = df['Spending Score (1-100)'].apply(dv.categorize_spending_score)
    contingency_table = pd.crosstab(df['Gender'], df['Spending_Category'])
    chi_square_test(contingency_table)

    # KNN Classifier with Visualization
    df = copy_df
    df['Spending Score (Category)'] = df['Spending Score (1-100)'].apply(dv.categorize_spending_score)
    print("\nKNN Classifier Performance:")
    accuracy, best_params = knn_classifier(
        data=df,
        target_column="Spending Score (Category)",  # Klassifikationsziel
    )
    print(f"Best Accuracy: {accuracy}")
    print(f"Best Parameters: {best_params}")

    print("\nK-Means Cluster Analysis:")
    cluster_centers = kmeans_cluster_analysis(df)

    # Add the cluster centers to the report
    data["cluster_centers"] = f"Cluster Centers: {cluster_centers}"

    # Return data for output generation
    return data