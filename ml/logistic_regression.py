from typing import Any

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from ml.evaluate_model import evaluate_model

def logistic_regression(data: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42) -> tuple[str, Any]:
    """
    Perform logistic regression classification on a given dataset.

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

    # Logistic regression model
    logreg = LogisticRegression(random_state=random_state)

    # Hyperparameter grid for GridSearchCV
    param_grid = {
        'C': [0.1, 1, 10, 100],  # Regularization strength
        'solver': ['liblinear', 'saga', 'newton-cg'],  # Solvers
        'max_iter': [100, 200, 300],  # Maximum iterations
    }

    # Set up GridSearchCV
    grid_search = GridSearchCV(estimator=logreg, param_grid=param_grid, cv=5, n_jobs=-1, verbose=0)

    # Fit the model with the best hyperparameters
    grid_search.fit(X_train, y_train)

    # Get the best model
    best_logreg = grid_search.best_estimator_

    # Evaluate the best model
    y_pred_logreg = best_logreg.predict(X_test)

    # Modell evaluieren
    return evaluate_model(y_test, y_pred_logreg), grid_search.best_params_
