import pandas as pd
from eda.visualisierungen import histogram, boxplot
from eda.statistiken import korrelation_kovarianz

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
        boxplot(data, x=column, y=None, hue=None, title=f"Boxplot of {column}", x_label=column, y_label=column[0], save_path="boxplot_{column}.png")

    # Korrelationen zwischen den Variablen
    # MaximaleHerzfrequenz/Alter ; Ruheblutdruck/Cholesterinwert ; Blutzucker/Cholesterinwert
    print(korrelation_kovarianz(data["MaximaleHerzfrequenz"], data["Alter"]))
    print(korrelation_kovarianz(data["Ruheblutdruck"], data["Cholesterinwert"]))
    print(korrelation_kovarianz(data["Blutzucker"], data["Cholesterinwert"]))

    # mögliche Zusammenhänge zwischen den unabhängigen Variablen und der Zielvariable
    # -> Alter/Gesundheitszustand
    ...

    # 2. Hypothesentests:
    # statistische Tests
    ...

    # Testen Sie, ob bestimmte Merkmale wie der Ruheblutdruck oder der Cholesterinwert signifikante Unterschiede zwischen Personen mit und ohne Risiko zeigen.
    ...

    # 3. Modellierung und Klassifikation:
    # Klassifikationsmodell
    ...

    # Evaluieren Sie die Modelle mit geeigneten Metriken (z.B. Accuracy, F1-Score).
    ...

    # Hyperparameter-Tuning
    ...

    # 4. Zusätzliche Analyse:
    # Wählen Sie ein Subset der Daten (z.B. eine spezifische Altersgruppe oder Geschlechtergruppe) und analysieren Sie, wie sich die Vorhersagen oder statistischen Eigenschaften in dieser Gruppe von der Gesamtpopulation unterscheiden.
    ...
