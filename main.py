import tkinter as tk
from tkinter import filedialog
import datenvorverarbeitung.datenvorverarbeitung as dv
import datensaetze_funktionen.kunden.kunden as kd
import datensaetze_funktionen.social_media.social_media as sm
import datensaetze_funktionen.gesundheitsdaten.gesundheitsdaten as gd

def select_file():
    """
    Opens a file dialog for the user to select a dataset.
    :return: The path to the selected file
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Wählen Sie eine Datendatei aus",
        filetypes=(("CSV-Dateien", "*.csv"), ("Textdateien", "*.txt"), ("PDF-Dateien", "*.pdf"), ("JSON-Dateien", "*.json") ,("Alle Dateien", "*.*"))
    )
    return file_path


if __name__ == "__main__":
    document = select_file()

    if document == "":
        print("Keine Datei ausgewählt. Das Programm wird beendet.")
        exit()

    df = dv.read_document(document)
    df = dv.replace_missing_values(df)
    df = dv.remove_duplicates(df)

    # Wähle das richtige Modul basierend auf dem Dateinamen
    if "Kunden-Datensatz" in document:
        kd.kunden_main(df)
    elif "Social-Media-Datensatz" in document:
        sm.social_media_main(df)
    elif "Gesundheitsdaten-Datensatz" in document:
        gd.gesundheitsdaten_main(df)
    else:
        print("Unbekannter Datensatz. Bitte einen gültigen Datensatz wählen.")