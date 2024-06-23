from instagrapi import Client
from instagrapi.exceptions import TwoFactorRequired
import networkx as nx
import matplotlib.pyplot as plt

# Set up Instagram client
instagram_client = Client()

# Set delay range (optional)
instagram_client.delay_range = [1, 5]

# Replace with your Instagram username and password
USERNAME = input("Input username: ")
PASSWORD = input("Input password: ")

assert USERNAME, 'Username should not be empty'
assert PASSWORD, 'Password should not be empty'

try:
    instagram_client.login(USERNAME, PASSWORD)
    print("Logged in successfully")
except TwoFactorRequired:
    print("Two-factor authentication required. Please disable it in your Instagram settings.")
    raise

# Fetch your followers
my_followers = instagram_client.user_followers(user_id=instagram_client.user_id)

# Create a graph
G = nx.Graph()

# Add yourself as a node
G.add_node(instagram_client.username, label=instagram_client.username)

# Add your followers as nodes and edges
for follower in my_followers.values():
    G.add_node(follower.username, label=follower.full_name)
    G.add_edge(instagram_client.username, follower.username)

# Save the graph in gexf format
nx.write_gexf(G, "InstaFollowers.gexf")
# Visualize the graph
plt.figure(figsize=(10, 10))  # Adjust figure size if needed
pos = nx.spring_layout(G, seed=42)  # Spring layout for better visualization

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_size=30, font_size=8, font_color='black')

# Save and show the graph
plt.savefig('InstaGraph.png', dpi=300)
plt.show()
density = nx.density(G)
print(f"Graph density: {density}")