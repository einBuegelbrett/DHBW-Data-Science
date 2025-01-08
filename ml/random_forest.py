import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from ml.evaluate_model import evaluate_model

def random_forest(data: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42):
    """
    Perform random forest classification on a given dataset.

    :param data: Input DataFrame
    :param target_column: The column to be predicted
    :param test_size: Proportion of the dataset to include in the test split
    :param random_state: Random state for reproducibility
    :return: Accuracy of the model
    """
    # Label encoding for the target column if it's categorical
    le = LabelEncoder()
    data[target_column] = le.fit_transform(data[target_column])

    # Splitting the data into features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Random forest model
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)

    # Modell evaluieren
    return evaluate_model(y_test, y_pred_rf)
