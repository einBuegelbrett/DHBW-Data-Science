import datenvorverarbeitung.datenvorverarbeitung as dv
import eda.statistiken as st
from eda.visualisierungen import scatterplot, boxplot, histogram, line_plot
from eda.test import chi_square_test, normality_test
from ml.k_neighbour import knn_classifier, kmeans_cluster_analysis
import pandas as pd

def categorize_spending_score(score):
    if score <= 33:
        return 'Low'
    elif score <= 66:
        return 'Medium'
    else:
        return 'High'
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
    df = dv.to_binary(df, "Gender", "Male", "Female")
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
    corr_cov = st.korrelation_kovarianz(df["Annual Income (k$)"], df["Spending Score (1-100)"])
    data["correlation_covariance"] = f"Covariance: {corr_cov['covariance']:.2f}, Correlation: {corr_cov['correlation']:.2f}"
    data["correlation_covariance_interpretation"] = (f"--- Analyse der Korrelation und Kovarianz ---<br>"
          f"Die Kovarianz {corr_cov['covariance']:.2f}, zeigt eine leichte gemeinsame Streuung der beiden Variablen,"
          f"was bedeutet, dass sie sich in die gleiche Richtung bewegen.<br>"
          "Die Stärke und Richtung der Beziehung wird dadurch aber nicht deutlich.<br>"
          f"Die Extrem niedrige Korrelation von {corr_cov['correlation']:f}, deutet darauf hin dass es keinen"
          "linearen Zusammenhang zwischen Einkommen und Ausgabenverhalten gibt.<br>")

    # Scatterplot: Income vs. Spending Score
    scatterplot(df, "Annual Income (k$)", "Spending Score (1-100)", "income_spending")
    data["scatterplot_interpretation"] = ("--- Interpretation des Scatterplots ---<br>"
        "Der Scatterplot zeigt deutlich unterschiedliche Cluster in den Daten: <br>"
          "Ein großes, zentrales Cluster, das viele Datenpunkte im Bereich von mittlerem Einkommen (40-60 k$) "
          "und mittlerem Spending Score (40-60) umfasst.<br>"
          "Vier kleinere Cluster, in den jeweiligen Ecken verteilt sind: "
          "Die Verteilung zeigt deutlich segmentiertes Verhalten, was auf verschiedene Kundengruppen oder "
          "Marktsegmente hinweist.")

    data["correlation_covariance_scatterplot"] = ("--- Verbindung zwischen Korrelation/Kovarianz und Scatterplot ---<br>"
            "Die numerischen Ergebnisse von Korrelation und Kovarianz stimmen mit dem Scatterplot überein:<br>"
            "Es gibt keinen linearen Zusammenhang zwischen Einkommen und Ausgabeverhalten, welcher Aussagekräftig genug ist"
            "um eine klare Beziehung zu erkennen.<br>"
            "Die Cluster im Scatterplot zeigen jedoch eine segmentierte Population, die sich in fünf Gruppen unterteilen lässt. "
            "Dies deutet darauf hin, dass andere Faktoren das Ausgabeverhalten beeinflussen. ")

    # Boxplot: Income by Gender
    boxplot(df, x="Gender", y="Annual Income (k$)", hue=None, title="Annual Income by Gender", x_label="Gender", y_label="Annual Income (k$)")

    # Normality Test
    print("\nNormality Test (Annual Income):")
    p_income = normality_test(df["Annual Income (k$)"])
    if p_income > 0.05:
        print("Annual Income data is normally distributed.")
    else:
        print("Annual Income data is not normally distributed.")

    # Chi-Square Test
    copy_df = df.copy()
    df['Spending_Category'] = df['Spending Score (1-100)'].apply(categorize_spending_score)

    # Create a contingency table for Gender vs. Spending_Category
    contingency_table = pd.crosstab(df['Gender'], df['Spending_Category'])

    # Perform the Chi-Square test
    print("\nChi-Square Test:")
    chi_square_test(contingency_table)

    # KNN Classifier with Visualization
    df = copy_df
    print("\nKNN Classifier Performance:")
    neighbors = [1, 3, 5]
    accuracies = []
    for n in neighbors:
        accuracy = knn_classifier(df, target_column="Spending Score (1-100)", n_neighbors=n)
        accuracies.append(accuracy)
        print(f"Accuracy with {n} neighbors: {accuracy:.2f}")

    # Lineplot for KNN Accuracies
    line_plot(x=neighbors, y=accuracies, title="KNN Accuracy vs. Number of Neighbors", x_label="Number of Neighbors", y_label="Accuracy")

    print("\nK-Means Cluster Analysis:")
    cluster_centers = kmeans_cluster_analysis(df)

    # Add the cluster centers to the report
    data["cluster_centers"] = f"Cluster Centers: {cluster_centers}"

    # Return data for output generation
    return data