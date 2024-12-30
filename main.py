import datenvorverarbeitung.datenvorverarbeitung as dv
import datensaetze_funktionen.kunden.kunden as kd
import datensaetze_funktionen.social_media.social_media as sm
import datensaetze_funktionen.gesundheitsdaten.gesundheitsdaten as gd

if __name__ == "__main__":
    document = "./datasets/Kunden-Datensatz.csv"
    df = dv.read_document(document)
    df = dv.replace_missing_values(df)
    df = dv.remove_duplicates(df)

    if document == "./datasets/Kunden-Datensatz.csv":
        kd.kunden_main(df)

    if document == "./datasets/Social-Media-Datensatz.csv":
        sm.social_media_main(df)

    if document == "./datasets/Gesundheitsdaten-Datensatz.txt":
        gd.gesundheitsdaten_main(df)