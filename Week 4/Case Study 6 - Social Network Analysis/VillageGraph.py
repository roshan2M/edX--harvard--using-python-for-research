import networkx as nx
import numpy as np

def load_village_relation_graphs() -> tuple:
    A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
    A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")
    G1 = nx.to_networkx_graph(A1)
    G2 = nx.to_networkx_graph(A2)
    return (G1, G2)

def basic_graph_stats(G: nx.Graph):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    print("Average degree: %.2f" % np.mean(list(dict(G.degree()).values())))

G1, G2 = load_village_relation_graphs()
basic_graph_stats(G1)
basic_graph_stats(G2)
