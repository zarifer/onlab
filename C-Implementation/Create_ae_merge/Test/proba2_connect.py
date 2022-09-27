import sys
import angr
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot
from pwnlib.elf.elf import ELF

p1 = angr.Project('/home/nimda/Documents/ml-sample-pack-small/benign/arm/3d2ba285d3eae9b06d6b893e7c102034ca898037ebc03d1fdf5c7504ad6bc9cb', load_options={'auto_load_libs':False})

cfg = p1.analyses.CFGFast()

G = cfg.graph
print(G)

#nx.draw(G)
#plt.show()

GS = ELF('/home/nimda/Documents/ml-sample-pack-small/benign/arm/3d2ba285d3eae9b06d6b893e7c102034ca898037ebc03d1fdf5c7504ad6bc9cb')
GSE = (hex(GS.entry))
print(GSE)
nx.draw(G, with_labels = False)
plt.show()

p2 = angr.Project('/home/nimda/Documents/ml-sample-pack-small/malware/arm/4eb6cb5191619d2d637beb4e6d4dde3aa58e7549b288f0d27916fe2ccd24be6a', load_options={'auto_load_libs':False})

cfg = p2.analyses.CFGFast()

H = cfg.graph
print(H)
nx.draw(H, with_labels = False)
plt.show()

HS = ELF('/home/nimda/Documents/ml-sample-pack-small/malware/arm/4eb6cb5191619d2d637beb4e6d4dde3aa58e7549b288f0d27916fe2ccd24be6a')
HSE = (hex(HS.entry))
print(HSE)

#nx.draw(H)
#plt.show()

F = nx.Graph()
F.add_node(7)
print(F)

#nx.draw(F)
#nx.draw(F, node_color = '#D00000')

F.add_nodes_from(G.nodes())
F.add_nodes_from(H.nodes())
F.add_edges_from(G.edges())
F.add_edges_from(H.edges())

F.add_edges_from([(7, list(G.nodes())[0]), (7, list(H.nodes())[0])])

write_dot(F, 'merged.dot')
nx.draw(F, with_labels = False)
plt.show()

