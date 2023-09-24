import networkx as nx
import random

def generate_random_graph(num_nodes, num_edges):
    graph = nx.gnm_random_graph(num_nodes, num_edges)
    return graph

# Example usage:
num_nodes = 10
num_edges = 15
random_graph = generate_random_graph(num_nodes, num_edges)
print(random_graph.nodes)
print(random_graph.edges)
