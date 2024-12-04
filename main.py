import datenvorverarbeitung as dv

if __name__ == "__main__":
    df = dv.read_document("./datasets/Social-Media-Datensatz.csv")
    print(df.head())