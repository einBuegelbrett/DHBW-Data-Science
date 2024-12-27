import pandas as pd

def read_document(filename: str) -> pd.DataFrame:
    """
    Read a document and return its content as a DataFrame.
    Supported file extensions: csv, txt (as comma-separated values)

    :param filename: Path to the document
    :return: DataFrame with the document content
    """
    extension = filename.split(".")[-1]
    match extension:
        case "csv":
            df = pd.read_csv(filename)
        case "txt":
            with open(filename, 'r') as file:
                # Read the first line as header and the rest as data
                header = file.readline().strip().split(",")
                data = [line.strip().split(",") for line in file]
            df = pd.DataFrame(data, columns=header)
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
