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

    return {"covariance": covariance, "correlation": correlation}
