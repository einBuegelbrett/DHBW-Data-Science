import pandas as pd
import numpy as np

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


def subset_analysis(data: pd.DataFrame, subset_condition: dict, target_variable: str) -> str:
    """
    Analyses a subset of the data and compares the characteristics with the total population.

    :param data: DataFrame with health data.
    :param subset_condition: Condition to filter a subset of the data (e.g. {‘Gender’: 1}).
    :return: A string containing the formatted analysis results.
    """
    # Initialize an empty string to hold the output
    output = ""

    # Konvertiere alle Spalten in numerische Werte
    data = data.apply(pd.to_numeric, errors='coerce')

    # Originaldaten untersuchen
    output += "<h2>--- Statistische Eigenschaften der Gesamtpopulation ---<\h2><br>"
    output += data.describe().to_html(classes="table")

    # Subset auswählen basierend auf der Bedingung
    subset = data.copy()
    for column, value in subset_condition.items():
        subset = subset[subset[column] == value]

    output += "<h2>--- Statistische Eigenschaften des Subsets ---<\h2><br>"
    output += subset.describe().to_html(classes="table")

    # Korrelationen innerhalb des Subsets
    output += "<h2>--- Korrelationen im Subset ---<\h2> <br>"
    for column in subset.columns[:-1]:
        if column != target_variable:
            corr_cov = korrelation_kovarianz(subset[column], subset[target_variable])
            output += f"Korrelation zwischen {column} und {target_variable} (Subset): {corr_cov['correlation']:.2f} (Kovarianz: {corr_cov['covariance']:.2f})<br>"

    return output

