from typing import Any
import pandas as pd
from pandas import DataFrame

def replace_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace missing values in a DataFrame with None.

    :param df: DataFrame
    :return: DataFrame with missing values replaced by None
    """
    if df.isnull().values.any():  # Check if there are any NaN values
        return df.where(pd.notnull(df), None)
    return df  # Return the original if no NaN is found


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from a DataFrame.

    :param df: Input DataFrame
    :return: DataFrame without duplicates
    """
    return df.drop_duplicates()


def to_binary(df: pd.DataFrame, column: str, word1: str, word2: str) -> pd.DataFrame:
    """
    Convert a column in a DataFrame to binary values (0 or 1).
    Maps 'word1' to 1 and 'word2' to 0.

    :param word1: Word to map to 1
    :param word2: Word to map to 0
    :param df: DataFrame
    :param column: Column name
    :return: DataFrame with binary column
    """
    mapping = {word1: 1, word2: 0}
    return df.assign(**{column: df[column].map(mapping)})


def map_keywords_to_integers(df: pd.DataFrame, column: str) -> tuple[DataFrame, dict[Any, int]]:
    """
    Map keywords in a column to unique integers.

    :param df: Input DataFrame
    :param column: Column name containing keywords
    :return: DataFrame with a new column for mapped integers
    """
    # Create a mapping of unique keywords to integers
    keyword_mapping = {keyword: idx for idx, keyword in enumerate(df[column].unique())}

    # Map the keywords in the DataFrame
    df[column] = df[column].map(keyword_mapping)

    return df, keyword_mapping


def clean_text(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Clean text data in a specified DataFrame column.

    :param df: Input DataFrame
    :param column: Column name containing text data
    :return: DataFrame with cleaned text in the specified column
    """
    df[column] = df[column].astype(str).str.lower() \
        .str.replace(r"http\S+", "", regex=True) \
        .str.replace(r"[^a-zA-Z0-9\s]", "", regex=True) \
        .str.replace(r"&amp;|amp", "", regex=True) \
        .str.replace(r"%20", " ", regex=True)
    return df

def categorize_spending_score(score: int) -> str:
    if score <= 33:
        return 'Low'
    elif score <= 66:
        return 'Medium'
    else:
        return 'High'

def categorize_herzfrequenz(value: int) -> str:
    if value < 120:
        return "Niedrig"
    elif 120 <= value <= 150:
        return "Mittel"
    else:
        return "Hoch"