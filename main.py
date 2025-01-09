import datenvorverarbeitung.data_cleaning as dv
import datensaetze_funktionen.kunden.kunden as kd
import datensaetze_funktionen.social_media.social_media as sm
import datensaetze_funktionen.gesundheitsdaten.gesundheitsdaten as gd
import datenvorverarbeitung.file_handler as fh
from jinja2 import Template
from templates.kunden_template import kunden_template
from templates.social_media_template import social_media_template
from templates.gesundheitsdaten_template import gesundheitsdaten_template
from xhtml2pdf import pisa

if __name__ == "__main__":
    document = fh.select_file()
    jinja_template = None
    data = None

    if document == "":
        print("Keine Datei ausgewählt. Das Programm wird beendet.")
        exit()

    jinja_template = None
    data = None

    df = fh.read_document(document)
    df = dv.replace_missing_values(df)
    df = dv.remove_duplicates(df)

    # Wähle das richtige Modul basierend auf dem Dateinamen
    if "Kunden-Datensatz" in document:
        data = kd.kunden_main(df)

        # Template laden
        jinja_template = Template(kunden_template)

    elif "Social-Media-Datensatz" in document:
        data = sm.social_media_main(df)

        # Template laden
        jinja_template = Template(social_media_template)

    elif "Gesundheitsdaten-Datensatz" in document:
        data = gd.gesundheitsdaten_main(df)

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

        def html_to_pdf(html_file, output_pdf):
            # Öffne die HTML-Datei und lese den Inhalt
            with open(html_file, "r", encoding="utf-8") as f:
                html_content = f.read()

            # Erstelle das PDF und speichere es im angegebenen Output-Pfad
            with open(output_pdf, 'wb') as pdf_file:
                pisa.CreatePDF(html_content, dest=pdf_file)


        # Nutze die Funktion mit der HTML-Datei und dem Ziel-PDF-Dateinamen
        html_to_pdf('report.html', 'report.pdf')
    else:
        print("Keine Template oder Daten gefunden.")