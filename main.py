from jinja2 import Template
from datensaetze_funktionen.gesundheitsdaten.gesundheitsdaten import gesundheitsdaten_main
from datensaetze_funktionen.kunden.kunden import kunden_main
from datensaetze_funktionen.social_media.social_media import social_media_main
from datenvorverarbeitung.datenbereinigung import replace_missing_values, remove_duplicates
from datenvorverarbeitung.datei_handler import read_document, select_file, html_to_pdf
from templates.kunden_template import kunden_template
from templates.social_media_template import social_media_template
from templates.gesundheitsdaten_template import gesundheitsdaten_template
from xhtml2pdf import pisa

if __name__ == "__main__":
    document = select_file()
    if document == "":
        print("Keine Datei ausgewählt. Das Programm wird beendet.")
        exit()

    jinja_template = None
    data = None

    # Lese die Datei ein und bereite sie vor, diese Schritte finden allgemein für alle Datensätze statt
    df = read_document(document)
    df = replace_missing_values(df)
    df = remove_duplicates(df)

    # Wähle das richtige Modul basierend auf dem Dateinamen
    if "Kunden-Datensatz" in document:
        data = kunden_main(df)

        # Template laden
        jinja_template = Template(kunden_template)

    elif "Social-Media-Datensatz" in document:
        data = social_media_main(df)

        # Template laden
        jinja_template = Template(social_media_template)

    elif "Gesundheitsdaten-Datensatz" in document:
        data = gesundheitsdaten_main(df)

        # Template laden
        jinja_template = Template(gesundheitsdaten_template)

    else:
        print("Unbekannter Datensatz. Bitte einen gültigen Datensatz wählen.")

    if jinja_template and data:

        html_to_pdf('report.html', 'report.pdf', jinja_template, data)
    else:
        print("Keine Template oder Daten gefunden.")