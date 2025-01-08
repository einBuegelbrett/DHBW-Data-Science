import datenvorverarbeitung.datenvorverarbeitung as dv
import datenvorverarbeitung.select_file as sf
import datensaetze_funktionen.kunden.kunden as kd
import datensaetze_funktionen.social_media.social_media as sm
import datensaetze_funktionen.gesundheitsdaten.gesundheitsdaten as gd
import datenvorverarbeitung.select_file as sf
from jinja2 import Template
from templates.kunden_template import kunden_template
from templates.social_media_template import social_media_template
from templates.gesundheitsdaten_template import gesundheitsdaten_template
import pdfkit

if __name__ == "__main__":
    document = sf.select_file()
    jinja_template = None
    data = None

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

        # Konvertiere HTML zu PDF
        pdfkit.from_file('report.html', 'report.pdf')
    else:
        print("Keine Template oder Daten gefunden.")