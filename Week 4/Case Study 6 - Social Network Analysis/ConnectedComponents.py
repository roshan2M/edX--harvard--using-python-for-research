from VillageGraph import load_village_relation_graphs

import matplotlib.pyplot as plt
import networkx as nx

def largest_connected_components(graph_list: list) -> list:
    lcc = []
    for graph in graph_list:
        gen = nx.connected_component_subgraphs(graph)
        lcc.append(max(gen, key=len))
    return lcc

def plot_largest_connected_components(graph_list: list) -> None:
    for index, graph in enumerate(graph_list):
        plt.figure()
        nx.draw(graph, node_color="red", edge_color="gray", node_size=20)
        plt.savefig("Village " + str(index+1) + " Graph.pdf")

graph_list = list(load_village_relation_graphs())
plot_largest_connected_components(graph_list)
