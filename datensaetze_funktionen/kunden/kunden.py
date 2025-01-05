import datenvorverarbeitung.datenvorverarbeitung as dv
import eda.statistiken as st
from eda.visualisierungen import scatterplot, boxplot, histogram, lineplot
from eda.test import chi_square_test, normality_test
from ml.k_neighbour import knn_classifier
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
    :return: None
    """
    print("Initial DataFrame:")
    print(df.head())

    # Encode Gender to binary
    df = dv.to_binary(df, "Gender", "Male", "Female")
    print("\nData after encoding Gender:")
    print(df.head())

# Die Oberen beiden Prints sind nur für die Ausgabe der Daten, um zu sehen, wie die Daten aussehen. Sollten vor Abgabe
# des Projekts entfernt werden.
    # Statistical Summary
    print("\nStatistical Summary:")
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
        elif col == "Annual Income (k$)":
            distribution_comment = "Die Verteilung des Einkommens ist relativ symmetrisch, da Median und Mittelwert fast gleich sind."
        elif col == "Spending Score (1-100)":
            distribution_comment = "Diese Verteilung ist nahezu ausgeglichen, was darauf hinweist, dass die Kunden unterschiedliche Kaufverhalten aufweisen, von sparsamen bis hin zu spendablen Kunden."
        else:
            distribution_comment = "Keine spezifische Verteilungsanalyse verfügbar."

        print(f"{col}:\n"
              f"  Mittelwert = {mean:.2f}\n"
              f"  Median = {median:.2f}\n"
              f"  Standardabweichung = {std_dev:.2f}\n"
              f"  {distribution_comment}\n")

    # Correlation and Covariance
    corr_cov = st.korrelation_kovarianz(df["Annual Income (k$)"], df["Spending Score (1-100)"])
    print("\n--- Analyse der Korrelation und Kovarianz ---")
    print(f"Die Kovarianz {corr_cov['covariance']:.2f}, zeigt eine leichte gemeinsame Streuung der beiden Variablen,was bedeutet, dass sie sich in die gleiche Richtung bewegen.\n"
          "Die Stärke und Richtung der Beziehung wird dadurch aber nicht deutlich.\n"
          f"Die Extrem niedrige Korrelation von {corr_cov['correlation']:f}, deutet darauf hin dass es keinen"
          "linearen Zusammenhang zwischen Einkommen und Ausgabenverhalten gibt.\n")
    # Scatterplot: Income vs. Spending Score
    scatterplot(df, "Annual Income (k$)", "Spending Score (1-100)")

    # Boxplot: Income by Gender
    boxplot(df, x="Gender", y="Annual Income (k$)", hue=None, title="Annual Income by Gender", x_label="Gender", y_label="Annual Income (k$)")

    # Histogram: Age Distribution
    histogram(df, column="Age", title="Age Distribution")

    # Histogram: Spending Score Distribution
    histogram(df, column="Spending Score (1-100)", title="Spending Score Distribution")

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
    neighbors = [1, 3, 5, 7, 9]
    accuracies = []
    for n in neighbors:
        accuracy = knn_classifier(df, target_column="Spending Score (1-100)", n_neighbors=n)
        accuracies.append(accuracy)
        print(f"Accuracy with {n} neighbors: {accuracy:.2f}")

    # Lineplot for KNN Accuracies
    lineplot(x=neighbors, y=accuracies, title="KNN Accuracy vs. Number of Neighbors", x_label="Number of Neighbors", y_label="Accuracy")