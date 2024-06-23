## Davydenko Pavlo IKM-M223b
# Lab 7: Instagram Followers Network Visualization Report

## Overview
* i have to create new account because i forgett my password)

This report details a Python script that connects to Instagram using the `instagrapi` library to visualize a network of your followers. It retrieves your followers, constructs a network graph using NetworkX, and visualizes the graph using Matplotlib.

## Code Explanation

### Import Libraries

```python
from instagrapi import Client
from instagrapi.exceptions import TwoFactorRequired
import networkx as nx
import matplotlib.pyplot as plt
```

### Set up Instagram Client

```python
instagram_client = Client()
instagram_client.delay_range = [1, 5]  # Optional: Set delay range
```

### Input Username and Password

```python
USERNAME = input("Input username: ")
PASSWORD = input("Input password: ")

assert USERNAME, 'Username should not be empty'
assert PASSWORD, 'Password should not be empty'
```

### Login to Instagram

Attempts to log in to Instagram using provided credentials and handles two-factor authentication if required:

```python
try:
    instagram_client.login(USERNAME, PASSWORD)
    print("Logged in successfully")
except TwoFactorRequired:
    print("Two-factor authentication required. Please disable it in your Instagram settings.")
    raise
```

### Fetch Followers

```python
my_followers = instagram_client.user_followers(user_id=instagram_client.user_id)
```

### Create Graph

Initializes a NetworkX graph and adds yourself as a node:

```python
G = nx.Graph()
G.add_node(instagram_client.username, label=instagram_client.username)
```

### Add Followers as Nodes and Edges

Iterates over your followers, adding each as a node and creating edges between yourself and each follower:

```python
for follower in my_followers.values():
    G.add_node(follower.username, label=follower.full_name)
    G.add_edge(instagram_client.username, follower.username)
```

### Visualize and Save Graph

Sets up visualization parameters, visualizes the graph using a spring layout, and saves the graph as an image:

```python
plt.figure(figsize=(10, 10))  # Adjust figure size if needed
pos = nx.spring_layout(G, seed=42)  # Spring layout for better visualization
nx.draw(G, pos, with_labels=True, node_size=30, font_size=8, font_color='black')
plt.savefig('InstaGraph.png', dpi=300)  # Save the graph as PNG
plt.show()  # Display the graph
```

### Calculate Graph Density

Calculates and prints the density of the graph:

```python
density = nx.density(G)
print(f"Graph density: {density}")
```

## Conclusion

This script provides a visualization of your Instagram followers network using NetworkX and Matplotlib. It demonstrates how to connect to Instagram, fetch data, construct a graph representation of followers, visualize the graph, and calculate basic properties like density. Adjustments can be made to customize the visualization or extend functionality based on specific needs.
