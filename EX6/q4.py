import math
import networkx as nx
import matplotlib.pyplot as plt

def negative_circle_graph(G):
    count = 0
    # Converts each weight to its logarithm
    for u, v, weight in G.edges.data('weight'):
        G.add_edge(u, v, weight=math.log2(weight))

    # Checking if there is a negative circle in the graph
    for v in G:
        try:
            negative_cycle = nx.find_negative_cycle(G, v)
            print("There is a negative cycle in the graph: =>", negative_cycle)
            show_graph(G)
            break
        except nx.NetworkXError:
            count += 1
    if(count == G.order()):
        print("There is no negative cycles in the graph!")


def show_graph(G):
    elarge = [(u, v) for (u, v, _) in G.edges(data=True)]
    pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=300)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2, alpha=0.5, edge_color="b", style="dashed")

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=13, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Negative Cycle
    Graph1 = nx.DiGraph()
    Graph1.add_weighted_edges_from([(0, 1, 2), (1, 4, 0.5), (4, 0, 0.5)])
    negative_circle_graph(Graph1)

    # No Negative Cycle
    Graph2 = nx.DiGraph()
    Graph2.add_weighted_edges_from([(0, 1, 2), (1, 4, 0.5), (4, 0, 2)])
    negative_circle_graph(Graph2)

    # Negative Cycle
    Graph3 = nx.DiGraph()
    Graph3.add_weighted_edges_from([(0, 1, 0.5), (1, 2, 2), (2, 3, 0.4), (3, 0, 2)])
    negative_circle_graph(Graph3)

    # No Negative Cycle
    Graph4 = nx.DiGraph()
    Graph4.add_weighted_edges_from([(0, 1, 2), (4, 0, 0.5)])
    negative_circle_graph(Graph4)

    # Negative Cycle
    Graph5 = nx.DiGraph()
    Graph5.add_weighted_edges_from([(0, 1, 2), (1, 2, 0.5), (2, 3, 0.4), (3, 0, 2), (2, 5, 4)])
    negative_circle_graph(Graph5)

    # No Negative Cycle
    Graph6 = nx.DiGraph()
    Graph6.add_weighted_edges_from([(0, 1, 2), (1, 0, 0.5)])
    negative_circle_graph(Graph6)

    # Negative Cycle
    Graph7 = nx.DiGraph()
    Graph7.add_weighted_edges_from([(0, 1, 1), (1, 0, 0.5)])
    negative_circle_graph(Graph7)


