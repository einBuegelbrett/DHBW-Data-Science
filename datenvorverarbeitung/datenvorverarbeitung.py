import pandas as pd
from PyPDF2 import PdfReader
import json

def read_document(filename: str) -> pd.DataFrame:
    """
    Read a document and return its content as a DataFrame.
    Supported file extensions: csv, pdf, txt, json

    :param filename: Path to the document
    :return: DataFrame with the document content
    """
    extension = filename.split(".")[-1]
    match extension:
        case "csv":
            df = pd.read_csv(filename)
        case "pdf":
            reader = PdfReader(filename)
            text = [page.extract_text() for page in reader.pages]
            df = pd.DataFrame({'Page': range(1, len(text) + 1), 'Content': text})
        case "txt":
            with open(filename, 'r') as file:
                lines = file.readlines()
            df = pd.DataFrame({'Line': range(1, len(lines) + 1), 'Content': [line.strip() for line in lines]})
        case "json":
            with open(filename, 'r') as file:
                data = json.load(file)
            df = pd.json_normalize(data)
        case _:
            raise ValueError(f"Unsupported file extension: {extension}")
    return df

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
