import pandas as pd
from datenvorverarbeitung.datenbereinigung import categorize_herzfrequenz
from eda.test import t_test_2_sample, normality_test, chi_square_test
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

    # Normality Test
    data["normality_test"] = normality_test(df, ['Gesundheitszustand'])
    data["which_test"] = ""
    data["test"] = ""

    if normality_test(df, ['Gesundheitszustand']) == "Gesundheitszustand is normally distributed.\n <br>":
        data["which_test"] = "Der Normality Test zeigt, dass die Zielvariable Gesundheitszustand normalverteilt ist und daher ein t-Test durchgeführt wird."
        data["test"] += "<h6>Nullhypothese (H₀): Es gibt keinen Unterschied im Gesundheitsrisiko zwischen Männern und Frauen.</h6>"
        data["test"] += t_test_2_sample(df["Gesundheitszustand"], df["Geschlecht"], alternative='two-sided')
        data["test"] += "Der Levene-Test zeigt mit einer P-Wert von 0.555, dass die Varianzen zwischen den Gruppen als gleich betrachtet werden können. Der Two-Sample T-Test liefert jedoch einen T-Wert von -3.62 und einen P-Wert von 0.0023, was darauf hinweist, dass die Nullhypothese abgelehnt wird. Es gibt also einen signifikanten Unterschied im Gesundheitsrisiko zwischen Männern und Frauen."
        data["test"] += "<h6>Nullhypothese (H₀): Es gibt keinen Unterschied im Cholesterinwert zwischen Personen mit Risiko (Gesundheitszustand = 1) und ohne Risiko (Gesundheitszustand = 0).</h6>"
        data["test"] += t_test_2_sample(df["Cholesterinwert"], df["Gesundheitszustand"], alternative='two-sided')
        data["test"] += "Auch hier zeigt der Levene-Test mit einem P-Wert von 0.00028 ungleiche Varianzen zwischen den Gruppen. Der T-Test liefert mit einem T-Wert von 14.85 und einem P-Wert von 4.17e-7 einen hochsignifikanten Unterschied. Dies bedeutet, dass der Cholesterinwert zwischen Personen mit und ohne Gesundheitsrisiko signifikant verschieden ist"
    else:
        data["which_test"] = "Der Normality Test zeigt, dass die Zielvariable Gesundheitszustand nicht normalverteilt ist und daher ein Chi-Square-Test durchgeführt wird."
        data["test"] += "<h6>Nullhypothese (H₀): Es gibt keinen Zusammenhang zwischen Geschlecht und Herzfrequenzkategorie.</h6>"
        df['Herzfrequenz_Kategorie'] = df['MaximaleHerzfrequenz'].apply(categorize_herzfrequenz)
        contingency_table = pd.crosstab(df['Geschlecht'], df['Herzfrequenz_Kategorie'])
        data["test"] = chi_square_test(contingency_table)
        data["test"] += "Der Chi-Quadrat-Test liefert einen Chi-Quadrat-Wert von 4.37 und einen P-Wert von 0.1124. Da der P-Wert größer als das übliche Signifikanzniveau von 0.05 ist, wird die Nullhypothese nicht abgelehnt. Das bedeutet, dass es keinen signifikanten Zusammenhang zwischen den Variablen gibt . Der Test zeigt, dass die  Kategorien nicht signifikant von den erwarteten Häufigkeiten abweichen. Es ist also nicht möglich, zu behaupten, dass das Geschlecht einen Einfluss auf die Herzfrequenzkategorie hat."


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