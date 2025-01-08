import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from ml.evaluate_model import evaluate_model
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

    # Predictions
    y_pred = knn.predict(X_test)

    # Accuracy
    accuracy = knn.score(X_test, y_test)
    print(f"KNN Accuracy: {accuracy}")

    # Evaluate model
    return evaluate_model(y_test, y_pred)


def kmeans_cluster_analysis(df, n_clusters=5):
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