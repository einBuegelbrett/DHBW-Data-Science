import tkinter as tk
from tkinter import filedialog
import datenvorverarbeitung.datenvorverarbeitung as dv
import eda.statistiken as st
import datensaetze_funktionen.kunden.kunden as kd
import datensaetze_funktionen.social_media.social_media as sm
import datensaetze_funktionen.gesundheitsdaten.gesundheitsdaten as gd
from jinja2 import Template
from eda.test import t_test_2_sample
from templates.kunden_template import kunden_template
from templates.social_media_template import social_media_template
from templates.gesundheitsdaten_template import gesundheitsdaten_template
import pdfkit

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


if __name__ == "__main__":
    document = select_file()

    if document == "":
        print("Keine Datei ausgewählt. Das Programm wird beendet.")
        exit()

    jinja_template = None
    data = None

    df = dv.read_document(document)
    df = dv.replace_missing_values(df)
    df = dv.remove_duplicates(df)

    # Wähle das richtige Modul basierend auf dem Dateinamen
    if "Kunden-Datensatz" in document:
        kd.kunden_main(df)
        # Daten vorbereiten
        data = {
            "initial_dataset": "Hier sind die Daten vor dem Cleaning beschrieben.",
            "cleaning": "Nach dem Cleaning wurden folgende Änderungen vorgenommen...",
            "correlation_covariance": "Die berechneten Korrelations- und Kovarianzwerte sind...",
            "graphs": "Graphen zur Visualisierung der Daten: ...",
            "tests": "Durchgeführte Tests und Ergebnisse: ...",
            "nlp_ml": "NLP- und ML-Techniken wie Tokenisierung und Modelltraining wurden angewandt...",
            "hyperparameter_tuning": "Ergebnisse des Hyperparametertunings: ..."
        }

        # Template laden
        jinja_template = Template(kunden_template)

    elif "Social-Media-Datensatz" in document:
        sm.social_media_main(df)

        initial_df = df.head()

        # Daten vorbereiten
        df, dict3 = dv.map_keywords_to_integers(df, "keyword")
        df, dict4 = dv.map_keywords_to_integers(df, "location")
        dv.clean_text(df, "keyword")
        dv.clean_text(df, "text")

        cleaned_df = df.head()

        dict1 = st.korrelation_kovarianz(df["keyword"], df["target"])
        dict2 = st.korrelation_kovarianz(df["location"], df["target"])

        # CODE FÜR VISUALISIERUNGEN HIER EINFÜGEN

        # Split into two groups
        relevant_posts = df[df['target'] == 1]['text_length']
        irrelevant_posts = df[df['target'] == 0]['text_length']

        # 2 sample t-test
        ttest = t_test_2_sample(relevant_posts, irrelevant_posts, alternative='two-sided')

        # CODE FÜR NLP UND HYPERPARAMETERTUNING HIER EINFÜGEN

        # Daten vorbereiten
        data = {
            "initial_dataset": initial_df,
            "cleaning": cleaned_df,
            "correlation_covariance": f"{dict1}, {dict2}",
            "graphs": "Graphen zur Visualisierung der Daten: ...",
            "tests": ttest,
            "nlp_ml": "NLP- und ML-Techniken wie Tokenisierung und Modelltraining wurden angewandt...",
            "hyperparameter_tuning": "Ergebnisse des Hyperparametertunings: ..."
        }

        # Template laden
        jinja_template = Template(social_media_template)

    elif "Gesundheitsdaten-Datensatz" in document:
        gd.gesundheitsdaten_main(df)
        # Daten vorbereiten
        data = {
            "initial_dataset": "Hier sind die Daten vor dem Cleaning beschrieben.",
            "cleaning": "Nach dem Cleaning wurden folgende Änderungen vorgenommen...",
            "correlation_covariance": "Die berechneten Korrelations- und Kovarianzwerte sind...",
            "graphs": "Graphen zur Visualisierung der Daten: ...",
            "tests": "Durchgeführte Tests und Ergebnisse: ...",
            "nlp_ml": "NLP- und ML-Techniken wie Tokenisierung und Modelltraining wurden angewandt...",
            "hyperparameter_tuning": "Ergebnisse des Hyperparametertunings: ..."
        }

        # Template laden
        jinja_template = Template(gesundheitsdaten_template)

    else:
        print("Unbekannter Datensatz. Bitte einen gültigen Datensatz wählen.")

    if jinja_template and data:
        # Template rendern
        rendered_html = jinja_template.render(**data)

        # HTML speichern
        with open("report.html", "w", encoding="utf-8") as f:
            f.write(rendered_html)

        # Konvertiere HTML zu PDF
        pdfkit.from_file('report.html', 'report.pdf')
    else:
        print("Kein Template gefunden.")