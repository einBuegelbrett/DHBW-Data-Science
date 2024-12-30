import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def knn_classifier(data: pd.DataFrame, target_column: str, n_neighbors: int = 5, test_size: float = 0.2, random_state: int = 42):
    """
    Perform K-Nearest Neighbors classification on a given dataset.

    :param data: Input DataFrame
    :param target_column: The column to be predicted
    :param n_neighbors: Number of neighbors for KNN
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

    # KNN model
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)

    # Accuracy
    accuracy = knn.score(X_test, y_test)
    print(f"KNN Accuracy: {accuracy}")
    return accuracy
