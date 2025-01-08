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


def count_outliers_iqr(series: pd.Series) -> int:
    """
    Count the number of outliers in a Series using the IQR method.

    :param series: Input Series
    :return: Number of outliers
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return ((series < lower_bound) | (series > upper_bound)).sum()


def gesundheitsdaten_subset_analysis(data: pd.DataFrame, subset_condition: dict) -> str:
    """
    Analyses a subset of the data and compares the characteristics with the total population.

    :param data: DataFrame with health data.
    :param subset_condition: Condition to filter a subset of the data (e.g. {‘Gender’: 1}).
    :return: A string containing the formatted analysis results.
    """
    # Initialize an empty string to hold the output
    output = ""

    # Konvertiere alle Spalten in numerische Werte
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    # Originaldaten untersuchen
    output += "<h2>--- Statistische Eigenschaften der Gesamtpopulation ---<\h2> <br>"
    output += f"{data.describe().to_string()} <br>"

    # Subset auswählen basierend auf der Bedingung
    subset = data.copy()
    for column, value in subset_condition.items():
        subset = subset[subset[column] == value]

    output += "<h2>--- Statistische Eigenschaften des Subsets ---<\h2> <br>"
    output += f"{subset.describe().to_string()} <br>"

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
    output += "<h2>--- Korrelationen im Subset ---<\h2> <br>"
    for column in subset.columns[:-1]:
        if column != "Gesundheitszustand":
            correlation, covariance = korrelation_kovarianz(subset[column], subset["Gesundheitszustand"])
            output += f"Korrelation zwischen {column} und Gesundheitszustand (Subset): {correlation:.2f} (Kovarianz: {covariance:.4f}) <br>"

    return output

