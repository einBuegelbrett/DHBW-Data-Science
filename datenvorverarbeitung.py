import pandas as pd
from PyPDF2 import PdfReader
import json

def read_document(fileName: str) -> pd.DataFrame:
    extension = fileName.split(".")[-1]
    match extension:
        case "csv":
            df = pd.read_csv(fileName)
        case "pdf":
            reader = PdfReader(fileName)
            text = [page.extract_text() for page in reader.pages]
            df = pd.DataFrame({'Page': range(1, len(text) + 1), 'Content': text})
        case "txt":
            with open(fileName, 'r') as file:
                lines = file.readlines()
            df = pd.DataFrame({'Line': range(1, len(lines) + 1), 'Content': [line.strip() for line in lines]})
        case "json":
            with open(fileName, 'r') as file:
                data = json.load(file)
            df = pd.json_normalize(data)
        case _:
            raise ValueError(f"Unsupported file extension: {extension}")
    return df
