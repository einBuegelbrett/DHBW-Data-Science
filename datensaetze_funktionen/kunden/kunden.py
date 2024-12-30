import datenvorverarbeitung.datenvorverarbeitung as dv
import eda.statistiken as st
from eda.visualisierungen import scatterplot, boxplot, histogram
from eda.test import t_test_1_sample, t_test_2_sample, chi_square_test
from ml.k_neighbour import knn_classifier
import pandas as pd

def kunden_main(df):
    """
    Main function to perform analysis on the customer dataset.

    :param df: Input DataFrame containing customer data
    :return: None
    """
    print(" DataFrame Head:")
    # Encode all Genders to binary
    df = dv.to_binary(df, "Gender", "Male", "Female")
    print(df.head())

    # Beispiel für Korrelation und Kovarianz
    dict = st.korrelation_kovarianz(df["Annual Income (k$)"], df["Spending Score (1-100)"])
    print(f"Korrelation und Kovarianz (Income vs. Spending Score): {dict}")

    # Scatterplot
    scatterplot(df, "Annual Income (k$)", "Spending Score (1-100)")

    # Boxplot
    boxplot(df, x="Gender", y="Annual Income (k$)", hue=None, title="Annual Income by Gender", x_label="Gender", y_label="Annual Income (k$)", save_path="boxplot_income_gender.png")

    # Normality Tests
    print("\nNormality Test (Income):")
    p = normality_test(df["Annual Income (k$)"])

    if p > 0.05:
        print("\nT-Test can be performed on the data for Income because it is normally distributed.")
    else:
        print("\nT-Test cannot be performed on the data for Income because it is not normally distributed.")

    # Chi-Square Test
    print("\nChi-Square Test:")
    gender_counts = pd.crosstab(index=df["Gender"], columns="count")
    chi_square_test(gender_counts)

    # Histogram: Spending Score
    histogram(df, column="Spending Score (1-100)", title="Spending Score Distribution")

    # KNN Classifier
    print("\nKNN Classifier:")
    accuracy = knn_classifier(df, target_column="Spending Score (1-100)", n_neighbors=5)
    print(f"KNN Model Accuracy: {accuracy}")
