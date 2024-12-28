import datenvorverarbeitung.datenvorverarbeitung as dv
import eda.statistiken as st
import eda.visualisierungen as vs

if __name__ == "__main__":
    document = "./datasets/Kunden-Datensatz.csv"
    df = dv.read_document(document)
    df = dv.replace_missing_values(df)
    df = dv.remove_duplicates(df)

    if document == "./datasets/Kunden-Datensatz.csv":
        df = dv.to_binary(df, "Gender", "Male", "Female")
        print(df.head())
        dict1 = st.korrelation_kovarianz(df["Gender"], df["Annual Income (k$)"])
        dict2 = st.korrelation_kovarianz(df["Spending Score (1-100)"], df["Annual Income (k$)"])
        # Bei beiden wenig Korrelation, da die Werte sehr nah an 0 sind.
        print(dict1) # Indicates a small positive relationship between the variables.
        print(dict2) # Indicates a stronger positive relationship between the variables (but the absolute value depends on the data's scale).
        vs.scatterplot(df, "Annual Income (k$)", "Spending Score (1-100)")
