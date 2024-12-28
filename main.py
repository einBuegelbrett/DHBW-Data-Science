import datenvorverarbeitung.datenvorverarbeitung as dv

if __name__ == "__main__":
    document = "./datasets/Social-Media-Datensatz.csv"
    df = dv.read_document(document)
    df = dv.replace_missing_values(df)
    df = dv.remove_duplicates(df)


