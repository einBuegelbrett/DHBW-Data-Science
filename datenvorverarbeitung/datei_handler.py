import pandas as pd
import tkinter as tk
from tkinter import filedialog
from xhtml2pdf import pisa


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


def select_file() -> str:
    """
    Opens a file dialog for the user to select a dataset.
    :return: The path to the selected file
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Wählen Sie eine Datendatei aus",
        filetypes=(("CSV-Dateien", "*.csv"), ("Textdateien", "*.txt"))
    )

    return file_path

def html_to_pdf(html_file: str, pdf_file: str, jinja_template: any, data: any):
    rendered_html = jinja_template.render(**data)

    # HTML speichern
    with open("report.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)

    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    with open(pdf_file, 'wb') as pdf_file:
        pisa.CreatePDF(html_content, dest=pdf_file)
