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

    # T-Test: One Sample
    print("\nOne-Sample T-Test (Income):")
    t_test_1_sample(df["Annual Income (k$)"], mu_0=50)

    # T-Test: Two Sample
    print("\nTwo-Sample T-Test (Income by Gender):")
    males_income = df[df["Gender"] == "Male"]["Annual Income (k$)"]
    females_income = df[df["Gender"] == "Female"]["Annual Income (k$)"]
    t_test_2_sample(males_income, females_income)

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
