## Davydenko Pavlo IKM-M223b
# Lab4: Binary Tree Visualization Report

## Overview

This report describes a Python script that visualizes a binary tree using NetworkX and Matplotlib. The script generates a random binary tree structure with 16 nodes (including the root) and plots it with labeled node values.

## Code Explanation

### Import Libraries

The script starts by importing necessary libraries:
- **numpy**: For generating random numbers.
- **matplotlib.pyplot**: For plotting.
- **networkx**: For creating and manipulating the graph structure.
  
```python
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
```

### TreeNode Class

Defines a `TreeNode` class representing each node in the binary tree:
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### add_node Function

Defines a function `add_node` to add nodes to the binary tree based on their values:
```python
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
```

### build_graph Function

Defines a function `build_graph` that recursively builds a directed graph (`DiGraph`) using NetworkX to represent the binary tree:
```python
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
```

### Generating and Adding Nodes

Generates a random number for the root and adds 15 random nodes to the binary tree:
```python
root_value = np.random.uniform(75, 300)
root = TreeNode(root_value)

for _ in range(15):
    value = np.random.uniform(75, 300)
    add_node(root, value)
```

### Visualization using NetworkX and Matplotlib

Builds the graph and positions, then plots the binary tree using NetworkX and Matplotlib:
```python
G, pos = build_graph(root)

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, labels={node: f"{node.value:.2f}" for node in G.nodes}, 
        node_size=700, node_color='lightblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray')
plt.title("Visualization of Binary Tree")

# Save the plot as PNG file
plt.savefig('binary_tree_visualization.png', format='png')

# Display the plot (optional)
plt.show()
```

### Explanation

- **TreeNode Class**: Represents each node in the binary tree with a value and pointers to left and right children.
- **add_node Function**: Adds nodes to the binary tree based on their values.
- **build_graph Function**: Recursively builds a directed graph using NetworkX to represent the binary tree structure.
- **Visualization**: Uses NetworkX to draw the graph and Matplotlib to customize and display the visualization. Each node is labeled with its value, and edges indicate parent-child relationships.

## Conclusion

This script demonstrates how to construct and visualize a binary tree structure using Python libraries. The resulting visualization is saved as `binary_tree_visualization.png`, providing a clear representation of the tree's hierarchical organization.

