import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from ml.evaluate_model import evaluate_model
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred_knn)

    # Confusion Matrix visualization
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', xticklabels=le.classes_, yticklabels=le.classes_)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Categories')
    plt.ylabel('Actual Categories')
    plt.savefig('images/knn_confusion_matrix.png')
    plt.show()

    # Return evaluation metrics and the best hyperparameters
    return evaluation_metrics, grid_search.best_params_


def kmeans_cluster_analysis(df: pd.DataFrame, n_clusters: int = 5) -> list:
    """
    Perform K-Means clustering on the dataset to identify potential customer segments.

    :param df: DataFrame containing the customer data
    :param n_clusters: Number of clusters to form
    :return: None (plots the results)
    """
    # Select relevant features for clustering (you can adjust this based on your data)
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

    # KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis', marker='o')
    plt.title(f"K-Means Clustering with {n_clusters} Clusters")
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.colorbar(label='Cluster')
    plt.savefig('images/kmeans_clusters.png')
    plt.show()

    # Cluster centers
    cluster_centers = kmeans.cluster_centers_
    print("Cluster Centers:", cluster_centers)

    return cluster_centers