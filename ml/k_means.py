import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def kmeans_cluster_analysis(df: pd.DataFrame, n_clusters: int, col1: str, col2: str) -> list:
    """
    Perform K-Means clustering on the dataset to identify potential customer segments.

    :param df: DataFrame containing the customer data
    :param n_clusters: Number of clusters to form
    :return: None (plots the results)
    """
    # Select relevant features for clustering (you can adjust this based on your data)
    x = df[[col1, col2]]

    # KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(x)

    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    plt.scatter(df[col1], df[col2], c=df['Cluster'], cmap='viridis', marker='o')
    plt.title(f"K-Means Clustering with {n_clusters} Clusters")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.colorbar(label='Cluster')
    plt.savefig('images/kmeans_clusters.png')
    plt.show()

    # Cluster centers
    cluster_centers = kmeans.cluster_centers_
    print("Cluster Centers:", cluster_centers)

    return cluster_centers