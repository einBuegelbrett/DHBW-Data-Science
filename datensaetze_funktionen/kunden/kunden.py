import datenvorverarbeitung.datenvorverarbeitung as dv
import eda.statistiken as st
from eda.visualisierungen import scatterplot, boxplot, histogram
from eda.test import t_test_1_sample, t_test_2_sample, chi_square_test
from ml.k_neighbour import knn_classifier
import pandas as pd

def kunden_main(df):
    df = dv.to_binary(df, "Gender", "Male", "Female")
    print(df.head())
    dict1 = st.korrelation_kovarianz(df["Gender"], df["Annual Income (k$)"])
    dict2 = st.korrelation_kovarianz(df["Spending Score (1-100)"], df["Annual Income (k$)"])
    # Bei beiden wenig Korrelation, da die Werte sehr nah an 0 sind.
    print(dict1)  # Indicates a small positive relationship between the variables.
    print(dict2)  # Indicates a stronger positive relationship between the variables (but the absolute value depends on the data's scale).
    vs.scatterplot(df, "Annual Income (k$)", "Spending Score (1-100)")
    # boxplot