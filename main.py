import datenvorverarbeitung.datenvorverarbeitung as dv
import datensaetze_funktionen.kunden.kunden as kd

if __name__ == "__main__":
    document = "./datasets/Kunden-Datensatz.csv"
    df = dv.read_document(document)
    df = dv.replace_missing_values(df)
    df = dv.remove_duplicates(df)

    if document == "./datasets/Kunden-Datensatz.csv":
        kd.kunden_main(df)
