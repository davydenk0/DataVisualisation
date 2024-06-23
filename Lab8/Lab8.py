import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA, TruncatedSVD, FactorAnalysis, KernelPCA
from sklearn.manifold import TSNE, MDS
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import os

# Read the CSV file into a DataFrame with correct decimal handling
df = pd.read_csv('KAHRAMAN.csv', delimiter=';', decimal=',')

# Separate features and target if applicable
data = df.iloc[:, :5].values  # Assuming first 5 columns are features

# Convert data to numerical format
data = data.astype(float)

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Create a directory to save plots if it does not exist
output_dir = 'plots'
os.makedirs(output_dir, exist_ok=True)


def calculate_inertia_2D(method, data):
    transformed = method.fit_transform(data)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(transformed)
    return kmeans, transformed


def calculate_inertia_3D(method, data):
    transformed = method.fit_transform(data)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(transformed)
    return kmeans, transformed


# List of dimensionality reduction methods for 2D and 3D
methods_2D = [
    (PCA(n_components=2), "PCA"),
    (TruncatedSVD(n_components=2), "TruncatedSVD"),
    (FactorAnalysis(n_components=2), "Factor Analysis"),
    (TSNE(n_components=2, random_state=42), "t-SNE"),
    (MDS(n_components=2, random_state=42), "MDS"),
    (KernelPCA(n_components=2, kernel='linear'), "Kernel PCA")
]

methods_3D = [
    (PCA(n_components=3), "PCA"),
    (TruncatedSVD(n_components=3), "TruncatedSVD"),
    (FactorAnalysis(n_components=3), "Factor Analysis"),
    (TSNE(n_components=3, random_state=42), "t-SNE"),
    (MDS(n_components=3, random_state=42), "MDS"),
    (KernelPCA(n_components=3, kernel='linear'), "Kernel PCA")
]


# Visualization function for 2D and 3D plots
def plot_clusters(method, transformed, kmeans, name, save_path=None):
    fig = plt.figure(figsize=(10, 6))

    if method.n_components == 2:
        plt.scatter(transformed[:, 0], transformed[:, 1], c=kmeans.labels_, cmap='viridis')
        plt.title(f'Clusters after {name} (2D)')
        plt.xlabel('Component 1')
        plt.ylabel('Component 2')
        plt.colorbar()
    elif method.n_components == 3:
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(transformed[:, 0], transformed[:, 1], transformed[:, 2], c=kmeans.labels_, cmap='viridis')
        ax.set_title(f'Clusters after {name} (3D)')
        ax.set_xlabel('Component 1')
        ax.set_ylabel('Component 2')
        ax.set_zlabel('Component 3')

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()


# Calculate inertia for 2D and visualize
print("Inertia for 2D:")
for method, name in methods_2D:
    kmeans, transformed = calculate_inertia_2D(method, data_scaled)
    inertia = kmeans.inertia_
    print(f"{name}: {inertia:.2f}")
    save_path = os.path.join(output_dir, f"{name}_2D.png")
    plot_clusters(method, transformed, kmeans, name, save_path=save_path)

# Calculate inertia for 3D and visualize
print("Inertia for 3D:")
for method, name in methods_3D:
    kmeans, transformed = calculate_inertia_3D(method, data_scaled)
    inertia = kmeans.inertia_
    print(f"{name}: {inertia:.2f}")
    save_path = os.path.join(output_dir, f"{name}_3D.png")
    plot_clusters(method, transformed, kmeans, name, save_path=save_path)
