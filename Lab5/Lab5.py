import networkx as nx
import scipy as sp
import matplotlib.pyplot as plt
import os
import subprocess
import sys

def get_tree(tree, G=nx.Graph(), itr=0, max_itr=900):
    point = tree.pop(0)
    itr += 1
    sub_tree = [
        os.path.join(point, x) for x in os.listdir(point)
        if os.path.isdir(os.path.join(point, x)) and not is_hidden_dir(os.path.join(point, x))
    ]
    if sub_tree:
        tree.extend(sub_tree)
        G.add_edges_from((point, b) for b in sub_tree)
    # Calculate the number of folders and files
    num_items = len(sub_tree)  # Number of folders
    num_items += len([x for x in os.listdir(point) if os.path.isfile(os.path.join(point, x))])
    # Add node to the graph with size based on number of items
    G.add_node(point, size=num_items)
    if tree and itr <= max_itr:
        return get_tree(tree, G, itr)
    else:
        return G

def is_hidden_dir(d):
    if sys.platform.startswith("win"):
        p = subprocess.check_output(["attrib", d.encode('cp1251', errors='replace')])
        p = p.decode('cp1251', errors='replace')  # decode the bytes to str
        return 'H' in p[:12]
    else:
        return os.path.basename(d).startswith('.')

def main(root_dir: str):
    G = get_tree(tree=[root_dir])

    options = {
        'node_color': 'blue',
        'node_size': [G.nodes[node]['size'] * 10 for node in G],  # Size based on number of items
        'width': 0.5,
        'with_labels': True,
        'alpha': 0.6,
        'font_size': 8,
        'font_family': 'Arial'
    }

    plt.figure(figsize=(12, 8))

    plt.subplot(221)
    plt.title('kamada_kawai')
    nx.draw_kamada_kawai(G, **options)

    plt.subplot(222)
    plt.title('circular')
    nx.draw_circular(G, **options)

    plt.subplot(223)
    plt.title('spectral')
    nx.draw_spectral(G, **options)

    plt.subplot(224)
    plt.title('spring')
    nx.draw_spring(G, **options)

    plt.tight_layout()
    plt.savefig('directory_graph.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    root_dir = r"D:\Docs"  # Replace with your root directory
    main(root_dir)
