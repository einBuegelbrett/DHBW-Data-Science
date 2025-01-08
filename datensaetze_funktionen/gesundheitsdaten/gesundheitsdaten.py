import pandas as pd
from eda.test import t_test_2_sample
from eda.visualisierungen import histogram, boxplot
from eda.statistiken import korrelation_kovarianz, gesundheitsdaten_subset_analysis
from ml.k_neighbour import knn_classifier
from ml.logistic_regression import logistic_regression
from ml.random_forest import random_forest


def gesundheitsdaten_main(df: pd.DataFrame):
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
    # TODO - Sich für eins Entscheiden
    print("\n--- Untersuchung der Verteilungen ---\n")
    for column in df.columns:
        histogram(df, column, column[0])

    # Ausreißer identifizieren
    for column in df.columns:
        boxplot(df, x=column, y=None, hue=None, title=f"Boxplot of {column}", x_label=column, y_label=column[0])

    # Correlation and covariance
    corr_cov_maximaleHerzfrequenz_alter = korrelation_kovarianz(df["MaximaleHerzfrequenz"], df["Alter"])
    corr_cov_ruheblutdruck_cholesterinwert = korrelation_kovarianz(df["Ruheblutdruck"], df["Cholesterinwert"])
    corr_cov_blutzucker_cholesterinwert = korrelation_kovarianz(df["Blutzucker"], df["Cholesterinwert"])
    data["corr_cov_maximaleHerzfrequenz_alter"] = f"Covariance: {corr_cov_maximaleHerzfrequenz_alter['covariance']:.2f}, Correlation: {corr_cov_maximaleHerzfrequenz_alter['correlation']:.2f}"
    data["corr_cov_ruheblutdruck_cholesterinwert"] = f"Covariance: {corr_cov_ruheblutdruck_cholesterinwert['covariance']:.2f}, Correlation: {corr_cov_ruheblutdruck_cholesterinwert['correlation']:.2f}"
    data["corr_cov_blutzucker_cholesterinwert"] = f"Covariance: {corr_cov_blutzucker_cholesterinwert['covariance']:.2f}, Correlation: {corr_cov_blutzucker_cholesterinwert['correlation']:.2f}"

    # mögliche Zusammenhänge zwischen den unabhängigen Variablen und der Zielvariable
    # TODO - Sich für eins Entscheiden
    print("\n--- Korrelationsanalyse ---\n")
    for column in df.columns[:-1]:  # Zielvariable ausschließen
        if column != "Gesundheitszustand":
            correlation, covariance = korrelation_kovarianz(df[column], df["Gesundheitszustand"])
            print(f"Korrelation zwischen {column} und Gesundheitszustand: {correlation:.2f} (Kovarianz: {covariance:.4f})")

    # 2. Hypothesentests:
    # statistische Tests
    ## Nullhypothese (H₀): Es gibt keinen Unterschied im Gesundheitsrisiko zwischen Männern und Frauen.
    t_test_2_sample(df["Gesundheitszustand"], df["Geschlecht"], alternative='two-sided')
    ## Nullhypothese (H₀): Es gibt keinen Unterschied im Gesundheitsrisiko zwischen den Altersgruppen.
    t_test_2_sample(df["Gesundheitszustand"], df["Alter"], alternative='two-sided')

    # Testen Sie, ob bestimmte Merkmale wie der Ruheblutdruck oder der Cholesterinwert signifikante Unterschiede zwischen Personen mit und ohne Risiko zeigen.
    ## Nullhypothese (H₀): Es gibt keinen Unterschied im Ruheblutdruck zwischen Personen mit Risiko (Gesundheitszustand = 1) und ohne Risiko (Gesundheitszustand = 0).
    t_test_2_sample(df["Ruheblutdruck"], df["Gesundheitszustand"], alternative='two-sided')
    ## Nullhypothese (H₀): Es gibt keinen Unterschied im Cholesterinwert zwischen Personen mit Risiko (Gesundheitszustand = 1) und ohne Risiko (Gesundheitszustand = 0).
    t_test_2_sample(df["Cholesterinwert"], df["Gesundheitszustand"], alternative='two-sided')

    # 3. Modellierung und Klassifikation:
    # Klassifikationsmodell
    X = df.drop("Gesundheitszustand", axis=1)  # Features
    # y = data["Gesundheitszustand"]  # Zielvariable
    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)

    # Evaluieren Sie die Modelle mit geeigneten Metriken (z.B. Accuracy, F1-Score) (findet statt in der Funktion).
    # logistic_regression
    logistic_regression(df, "Gesundheitszustand")
    # random_forest
    random_forest(df, "Gesundheitszustand")
    # knn_classifier
    knn_classifier(df, "Gesundheitszustand")


    # Hyperparameter-Tuning
    ...

    # 4. Zusätzliche Analyse:
    # Wählen Sie ein Subset der Daten (z.B. eine spezifische Altersgruppe oder Geschlechtergruppe) und analysieren Sie, wie sich die Vorhersagen oder statistischen Eigenschaften in dieser Gruppe von der Gesamtpopulation unterscheiden.
    subset_condition = {'Alter': 60}
    gesundheitsdaten_subset_analysis(df, subset_condition)