import tkinter as tk
from tkinter import filedialog

def select_file():
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