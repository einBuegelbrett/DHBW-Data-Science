import pandas as pd
from eda.test import t_test_2_sample
from eda.visualisierungen import histogram, boxplot
from eda.statistiken import korrelation_kovarianz, gesundheitsdaten_subset_analysis
from ml.k_neighbour import knn_classifier
from ml.logistic_regression import logistic_regression
from ml.random_forest import random_forest


def gesundheitsdaten_main(data: pd.DataFrame):
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    # 1. Datenexploration (EDA):
    # Untersuchung der Verteilung der numerischen Variablen
    print("\n--- Untersuchung der Verteilungen ---\n")
    for column in data.columns:
        histogram(data, column, column[0])

    # Ausreißer identifizieren
    for column in data.columns:
        boxplot(data, x=column, y=None, hue=None, title=f"Boxplot of {column}", x_label=column, y_label=column[0])

    # Korrelationen zwischen den Variablen
    # MaximaleHerzfrequenz/Alter ; Ruheblutdruck/Cholesterinwert ; Blutzucker/Cholesterinwert
    print(korrelation_kovarianz(data["MaximaleHerzfrequenz"], data["Alter"]))
    print(korrelation_kovarianz(data["Ruheblutdruck"], data["Cholesterinwert"]))
    print(korrelation_kovarianz(data["Blutzucker"], data["Cholesterinwert"]))

    # mögliche Zusammenhänge zwischen den unabhängigen Variablen und der Zielvariable
    print("\n--- Korrelationsanalyse ---\n")
    for column in data.columns[:-1]:  # Zielvariable ausschließen
        if column != "Gesundheitszustand":
            correlation, covariance = korrelation_kovarianz(data[column], data["Gesundheitszustand"])
            print(f"Korrelation zwischen {column} und Gesundheitszustand: {correlation:.2f} (Kovarianz: {covariance:.4f})")

    # 2. Hypothesentests:
    # statistische Tests
    ## Nullhypothese (H₀): Es gibt keinen Unterschied im Gesundheitsrisiko zwischen Männern und Frauen.
    t_test_2_sample(data["Gesundheitszustand"], data["Geschlecht"], alternative='two-sided')
    ## Nullhypothese (H₀): Es gibt keinen Unterschied im Gesundheitsrisiko zwischen den Altersgruppen.
    t_test_2_sample(data["Gesundheitszustand"], data["Alter"], alternative='two-sided')

    # Testen Sie, ob bestimmte Merkmale wie der Ruheblutdruck oder der Cholesterinwert signifikante Unterschiede zwischen Personen mit und ohne Risiko zeigen.
    ## Nullhypothese (H₀): Es gibt keinen Unterschied im Ruheblutdruck zwischen Personen mit Risiko (Gesundheitszustand = 1) und ohne Risiko (Gesundheitszustand = 0).
    t_test_2_sample(data["Ruheblutdruck"], data["Gesundheitszustand"], alternative='two-sided')
    ## Nullhypothese (H₀): Es gibt keinen Unterschied im Cholesterinwert zwischen Personen mit Risiko (Gesundheitszustand = 1) und ohne Risiko (Gesundheitszustand = 0).
    t_test_2_sample(data["Cholesterinwert"], data["Gesundheitszustand"], alternative='two-sided')

    # 3. Modellierung und Klassifikation:
    # Klassifikationsmodell
    X = data.drop("Gesundheitszustand", axis=1)  # Features
    # y = data["Gesundheitszustand"]  # Zielvariable
    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)

    # Evaluieren Sie die Modelle mit geeigneten Metriken (z.B. Accuracy, F1-Score) (findet statt in der Funktion).
    # logistic_regression
    logistic_regression(data, "Gesundheitszustand")
    # random_forest
    random_forest(data, "Gesundheitszustand")
    # knn_classifier
    knn_classifier(data, "Gesundheitszustand")


    # Hyperparameter-Tuning
    ...

    # 4. Zusätzliche Analyse:
    # Wählen Sie ein Subset der Daten (z.B. eine spezifische Altersgruppe oder Geschlechtergruppe) und analysieren Sie, wie sich die Vorhersagen oder statistischen Eigenschaften in dieser Gruppe von der Gesamtpopulation unterscheiden.
    subset_condition = {'Alter': 60}
    gesundheitsdaten_subset_analysis(data, subset_condition)