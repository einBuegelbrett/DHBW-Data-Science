import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def relative_haeufigkeit(data: pd.Series) -> pd.Series:
    """
    Calculate the relative frequency of each unique value in a Series.

    :param data: Input Series
    :return: Series with the relative frequencies
    """
    return data.value_counts(normalize=True)


def mittelwert(data: pd.Series) -> float:
    """
    Calculate the arithmetic mean of a Series.

    :param data: Input Series
    :return: Arithmetic mean
    """
    return data.mean()


def median(data: pd.Series) -> float:
    """
    Calculate the median of a Series.

    :param data: Input Series
    :return: Median
    """
    return data.median()


def modus(data: pd.Series) -> float:
    """
    Calculate the mode of a Series.

    :param data: Input Series
    :return: Mode
    """
    return data.mode().iloc[0]


def korrelation_kovarianz(series1: pd.Series, series2: pd.Series) -> dict:
    """
    Calculate the correlation and covariance between two Series.

    :param series1: First input Series
    :param series2: Second input Series
    :return: Dictionary with 'correlation' and 'covariance'
    """
    if len(series1) != len(series2):
        raise ValueError("Both Series must have the same length.")

    # Berechnung der Kovarianz
    covariance = np.cov(series1, series2)[0, 1]

    # Berechnung der Korrelation
    correlation = np.corrcoef(series1, series2)[0, 1]

    result = {'covariance': covariance, 'correlation': correlation}
    cleaned_result = {key: float(value) for key, value in result.items()}

    return cleaned_result


def gesundheitsdaten_subset_analysis(data: pd.DataFrame, subset_condition: dict):
    """
    Analysiert ein Subset der Daten und vergleicht die Eigenschaften mit der Gesamtpopulation.

    :param data: DataFrame mit Gesundheitsdaten.
    :param subset_condition: Bedingung, um ein Subset der Daten zu filtern (z. B. {'Geschlecht': 1}).
    """
    # Konvertiere alle Spalten in numerische Werte
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    # Originaldaten untersuchen
    print("\n--- Statistische Eigenschaften der Gesamtpopulation ---\n")
    print(data.describe())

    # Subset auswählen basierend auf der Bedingung
    subset = data.copy()
    for column, value in subset_condition.items():
        subset = subset[subset[column] == value]

    print("\n--- Statistische Eigenschaften des Subsets ---\n")
    print(subset.describe())

    # Histogramme: Vergleich zwischen Gesamtpopulation und Subset
    for column in data.columns:
        plt.figure(figsize=(12, 6))
        sns.histplot(data[column], color="blue", kde=True, bins=20, label="Gesamtpopulation", alpha=0.6)
        sns.histplot(subset[column], color="orange", kde=True, bins=20, label="Subset", alpha=0.6)
        plt.title(f"Verteilung von {column} (Gesamtpopulation vs. Subset)")
        plt.xlabel(column)
        plt.ylabel("Häufigkeit")
        plt.legend()
        plt.show()

    # Boxplots: Vergleich zwischen Gesamtpopulation und Subset
    for column in data.columns[:-1]:  # Zielvariable ausschließen
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=pd.concat([data, subset.assign(Group="Subset")]), x="Gesundheitszustand", y=column, hue="Group")
        plt.title(f"Boxplot von {column} vs. Gesundheitszustand (Gesamtpopulation vs. Subset)")
        plt.xlabel("Gesundheitszustand (0 = Gesund, 1 = Krank)")
        plt.ylabel(column)
        plt.show()

    # Korrelationen innerhalb des Subsets
    print("\n--- Korrelationen im Subset ---\n")
    for column in subset.columns[:-1]:
        if column != "Gesundheitszustand":
            correlation, covariance = korrelation_kovarianz(subset[column], subset["Gesundheitszustand"])
            print(f"Korrelation zwischen {column} und Gesundheitszustand (Subset): {correlation:.2f} (Kovarianz: {covariance:.4f})")

