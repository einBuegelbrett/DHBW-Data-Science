import pandas as pd
from eda.test import t_test_2_sample
from eda.visualisierungen import histogram, boxplot
from eda.statistiken import korrelation_kovarianz, gesundheitsdaten_subset_analysis, count_outliers_iqr
from ml.k_neighbour import knn_classifier
from ml.logistic_regression import logistic_regression
from ml.random_forest import random_forest

def gesundheitsdaten_main(df: pd.DataFrame) -> dict[str, str]:
    """
    Main function to perform analysis on the health data dataset.

    :param df: Input DataFrame containing health data data
    :return: Data Input for output generation
    """
    data = {}
    data["initial_dataset"] = df.head().to_html(classes="table")

    # Data Cleaning
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    data["cleaning"] = df.head().to_html(classes="table")

    # 1. Datenexploration (EDA):
    # Untersuchung der Verteilung der numerischen Variablen
    for column in df.columns:
        print("Column: ", column)
        histogram(df, column, column, column)

    # Ausreißer identifizieren
    # Anzahl der Ausreißer für jede Spalte berechnen
    outlier_counts = {col: count_outliers_iqr(df[col]) for col in df.columns}

    # Sortieren und die drei Spalten mit den meisten Ausreißern auswählen
    top_outliers = sorted(outlier_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    # Ausgabe der Top-3-Spalten
    i = 0
    data["top_outliers"] = ""
    for column, count in top_outliers:
        data["top_outliers"] += f"<li>{column}: {count} Ausreißer</li>"
        boxplot(df, x=column, y=None, hue=None, title=f"Boxplot of {column}", x_label=column, y_label=column[0],
                image_name=f"image_{i}")
        i+= 1

    # Correlation and covariance
    corr_cov_maximaleHerzfrequenz_alter = korrelation_kovarianz(df["MaximaleHerzfrequenz"], df["Alter"])
    corr_cov_ruheblutdruck_cholesterinwert = korrelation_kovarianz(df["Ruheblutdruck"], df["Cholesterinwert"])
    corr_cov_blutzucker_cholesterinwert = korrelation_kovarianz(df["Blutzucker"], df["Cholesterinwert"])
    data["corr_cov_maximaleHerzfrequenz_alter"] = f"Covariance: {corr_cov_maximaleHerzfrequenz_alter['covariance']:.2f}, Correlation: {corr_cov_maximaleHerzfrequenz_alter['correlation']:.2f}"
    data["corr_cov_ruheblutdruck_cholesterinwert"] = f"Covariance: {corr_cov_ruheblutdruck_cholesterinwert['covariance']:.2f}, Correlation: {corr_cov_ruheblutdruck_cholesterinwert['correlation']:.2f}"
    data["corr_cov_blutzucker_cholesterinwert"] = f"Covariance: {corr_cov_blutzucker_cholesterinwert['covariance']:.2f}, Correlation: {corr_cov_blutzucker_cholesterinwert['correlation']:.2f}"

    # mögliche Zusammenhänge zwischen den unabhängigen Variablen und der Zielvariable
    # Dictionary zur Speicherung der Korrelationen
    correlations = {}
    for column in df.columns[:-1]:  # Zielvariable ausschließen
        if column != "Gesundheitszustand":
            corr_cov = korrelation_kovarianz(df[column], df["Gesundheitszustand"])
            correlations[column] = corr_cov['covariance']
            f"Covariance: {corr_cov['covariance']:.2f}, Correlation: {corr_cov['correlation']:.2f}"

    # Bestimmung der höchsten und niedrigsten Korrelation
    max_correlation_column = max(correlations, key=correlations.get)
    min_correlation_column = min(correlations, key=correlations.get)

    # Ausgabe der Spalten mit der höchsten und niedrigsten Korrelation
    data["max_correlation_column"] = f"Spalte mit der größten Korrelation: {max_correlation_column} ({correlations[max_correlation_column]:.2f})"
    data["min_correlation_column"] = f"Spalte mit der niedrigsten Korrelation: {min_correlation_column} ({correlations[min_correlation_column]:.2f})"

    # 2. Hypothesentests:
    # statistische Tests
    data["ttest_Gesundheitszustand_Geschlecht"] = t_test_2_sample(df["Gesundheitszustand"], df["Geschlecht"], alternative='two-sided')
    data["ttest_Gesundheitszustand_Alter"] = t_test_2_sample(df["Gesundheitszustand"], df["Alter"], alternative='two-sided')
    # Testen Sie, ob bestimmte Merkmale wie der Ruheblutdruck oder der Cholesterinwert signifikante Unterschiede zwischen Personen mit und ohne Risiko zeigen.
    data["ttest_Ruheblutdruck_Gesundheitszustand"] = t_test_2_sample(df["Ruheblutdruck"], df["Gesundheitszustand"], alternative='two-sided')
    data["ttest_Cholesterinwert_Gesundheitszustand"] = t_test_2_sample(df["Cholesterinwert"], df["Gesundheitszustand"], alternative='two-sided')

    # 3. Modellierung und Klassifikation:
    # Klassifikationsmodell
    # Evaluieren Sie die Modelle mit geeigneten Metriken (z.B. Accuracy, F1-Score) (findet statt in der Funktion).
    # logistic_regression
    data["logistic_regression_evaluate_model"], data["logistic_regression_best_params"] = logistic_regression(df, "Gesundheitszustand")
    # random_forest
    data["random_forest_evaluate_model"], data["random_forest_best_params"] = random_forest(df, "Gesundheitszustand")
    # knn_classifier
    data["knn_classifier_evaluate_model"], data["knn_classifier_best_params"] = knn_classifier(df, "Gesundheitszustand")

    # 4. Zusätzliche Analyse:
    # Wählen Sie ein Subset der Daten (z.B. eine spezifische Altersgruppe oder Geschlechtergruppe) und analysieren Sie, wie sich die Vorhersagen oder statistischen Eigenschaften in dieser Gruppe von der Gesamtpopulation unterscheiden.
    # TODO - String zurückgeben
    subset_condition = {'Alter': 60}
    # data["mehranalyse"] = gesundheitsdaten_subset_analysis(df, subset_condition)

    # Return data for output generation
    return data