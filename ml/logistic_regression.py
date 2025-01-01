import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def logistic_regression(data: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42):
    """
    Perform logistic regression classification on a given dataset.

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

    # Logistic regression model
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    y_pred_logreg = logreg.predict(X_test)

    # Accuracy
    print("Logistische Regression")
    print(classification_report(y_test, y_pred_logreg))
    print(f"Accuracy: {accuracy_score(y_test, y_pred_logreg)}")
