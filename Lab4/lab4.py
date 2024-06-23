import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add_node(root, value):
    if value < root.value:
        if root.left is None:
            root.left = TreeNode(value)
        else:
            add_node(root.left, value)
    else:
        if root.right is None:
            root.right = TreeNode(value)
        else:
            add_node(root.right, value)

def build_graph(root):
    graph = nx.DiGraph()
    positions = {}

    def recurse(node, x=0, y=0, level=0):
        if node:
            graph.add_node(node)
            positions[node] = (x, y)

            if node.left:
                graph.add_edge(node, node.left)
                recurse(node.left, x - 1 / 2 ** (level + 1), y - 1, level + 1)

            if node.right:
                graph.add_edge(node, node.right)
                recurse(node.right, x + 1 / 2 ** (level + 1), y - 1, level + 1)

    recurse(root)
    return graph, positions

# Generate a random number within [75, 300] for the root
root_value = np.random.uniform(75, 300)
root = TreeNode(root_value)

# Add 15 random nodes within [75, 300] to the tree
for _ in range(15):
    value = np.random.uniform(75, 300)
    add_node(root, value)

# Build the graph and positions
G, pos = build_graph(root)

# Plotting the tree using NetworkX and Matplotlib
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, labels={node: f"{node.value:.2f}" for node in G.nodes}, node_size=700, node_color='lightblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray')
plt.title("Visualization of Binary Tree")

# Save the plot as PNG file
plt.savefig('binary_tree_visualization.png', format='png')

# Display the plot (optional)
plt.show()
