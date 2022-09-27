import angr
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from([1, 3])
G.add_edges_from([(1, 2), (2, 3)])
nx.draw_networkx(G, with_labels = True)
plt.show()

H = nx.DiGraph()
H.add_nodes_from([4, 6])
H.add_edges_from([(4, 5), (5, 6)])
nx.draw_networkx(H, with_labels = True)
plt.show()

F = nx.DiGraph()
F.add_node(7)
nx.draw_networkx(F, with_labels = True)
plt.show()

F.add_nodes_from(G.nodes())
F.add_nodes_from(H.nodes())
F.add_edges_from(G.edges())
F.add_edges_from(H.edges())

F.add_edges_from([(7, list(G.nodes())[0]), (7, list(H.nodes())[0])])

nx.draw_networkx(F, with_labels = True)
plt.show()
