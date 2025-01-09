import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from ml.evaluate_model import evaluate_model
from ml.confusion_matrix import confusion_matrix_plot

def knn_classifier(data: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42) -> tuple[str, dict]:
    """
    Perform K-Nearest Neighbors classification on a given dataset.

    :param data: Input DataFrame
    :param target_column: The column to be predicted
    :param test_size: Proportion of the dataset to include in the test split
    :param random_state: Random state for reproducibility
    :return: Best model and its evaluation score
    """
    # Label encoding for the target column if it's categorical
    le = LabelEncoder()
    data[target_column] = le.fit_transform(data[target_column])

    # Splitting the data into features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Define the KNN model
    knn = KNeighborsClassifier()

    # Hyperparameter grid for GridSearchCV
    param_grid = {
        'n_neighbors': [3, 5, 7, 9, 11],
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan', 'minkowski'],
        'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
    }

    # Set up GridSearchCV
    grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, cv=5, n_jobs=-1, verbose=0)

    # Fit the model with the best hyperparameters
    grid_search.fit(X_train, y_train)

    # Get the best model
    best_knn = grid_search.best_estimator_

    # Evaluate the best model
    y_pred_knn = best_knn.predict(X_test)

    # Evaluate the model with existing metrics (recall, f1-score, accuracy)
    evaluation_metrics = evaluate_model(y_test, y_pred_knn)

    #Confusion Matrix
    confusion_matrix_plot(y_test, y_pred_knn, le)

    # Return evaluation metrics and the best hyperparameters
    return evaluation_metrics, grid_search.best_params_
