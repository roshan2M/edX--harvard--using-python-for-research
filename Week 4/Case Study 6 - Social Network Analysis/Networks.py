from scipy.stats import bernoulli

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def er_graph(N: int, p: float) -> nx.Graph:
    """
    Generates an Erdos-Renyi random graph model.
    """
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for u in G.nodes():
        for v in G.nodes():
            if u < v and bernoulli.rvs(p=p):
                G.add_edge(u, v)
    return G

def plot_degree_distribution(G: nx.Graph, file_name: str):
    plt.hist(list(dict(G.degree()).values()), histtype="step")
    plt.title("Degree Distribution of Graph $G$")
    plt.xlabel("Degree $k$")
    plt.ylabel("Frequency")
    plt.savefig(file_name)

def generate_er_graph():
    G = er_graph(50, 0.08)
    nx.draw(G, node_size=40, node_color="gray")
    plt.savefig("Randomly Generated ER Graph.pdf")

def generate_karate_club_graph():
    T = nx.karate_club_graph()
    nx.draw(T, with_labels=True, node_color="lightblue", edge_color="green")
    plt.savefig("Karate Club Relational Graph.pdf")
