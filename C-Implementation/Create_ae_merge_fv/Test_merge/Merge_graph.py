import sys
import angr
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot

p1 = angr.Project('/home/nimda/Documents/ml-sample-pack-small/benign/arm/3d2ba285d3eae9b06d6b893e7c102034ca898037ebc03d1fdf5c7504ad6bc9cb', load_options={'auto_load_libs':False})

cfg = p1.analyses.CFGFast()

G = cfg.graph
print(G)

p2 = angr.Project('/home/nimda/Documents/ml-sample-pack-small/malware/arm/4eb6cb5191619d2d637beb4e6d4dde3aa58e7549b288f0d27916fe2ccd24be6a', load_options={'auto_load_libs':False})

cfg = p2.analyses.CFGFast()

H = cfg.graph
print(H)

F = nx.compose(G, H)
print(F)

write_dot(F, 'merged.dot')
nx.draw(F)
plt.savefig("merged_graph.png")

with open('merged.txt', 'w') as f:

	#Number of edges in the graph
	f.write(str(nx.number_of_edges(F))+"\n")

	#Number of nodes in the graph
	f.write(str(nx.number_of_nodes(F))+"\n")

	#The density of a graph
	f.write(str(nx.density(F))+"\n")
				
	#The number of components
	f.write(str(nx.number_strongly_connected_components(F))+"\n")

	#The shortest path length
	sp = dict(nx.all_pairs_shortest_path_length(F))
	#f.write(str(sp))

	#The minimum of shortest path
	df =  [np.min(list(spl.values())) for spl in sp.values()]
	f.write(str(np.min(df))+"\n")

	#The maximum of shortest path
	df = [np.max(list(spl.values())) for spl in sp.values()]
	f.write(str(np.max(df))+"\n")

	#The median of shortest path
	df = []
	for spl in sp.values():
		df += spl.values()
	f.write(str(np.median(df))+"\n")

	#The mean of shortest path
	df = []
	for spl in sp.values():
		df += spl.values()
	f.write(str(np.mean(df))+"\n")

	#The standard deviation of shortest path
	df = []
	for spl in sp.values():
		df += spl.values()
	f.write(str(np.std(df))+"\n")
				
	#The Betweenness Centrality of the graph
	bc = nx.centrality.betweenness_centrality(F)
				
	#The minimum of BC
	f.write(str(np.min(list(bc.values())))+"\n")

	#The maximum of BC
	f.write(str(np.max(list(bc.values())))+"\n")

	#The median of BC
	f.write(str(np.median(list(bc.values())))+"\n")

	#The mean of BC
	f.write(str(np.mean(list(bc.values())))+"\n")

	#The standard deviation of BC
	f.write(str(np.std(list(bc.values())))+"\n")

	#The Closeness Centrality of the graph
	cc = nx.centrality.closeness_centrality(F)
				
	#The minimum of CC
	f.write(str(np.min(list(cc.values())))+"\n")

	#The maximum of CC
	f.write(str(np.max(list(cc.values())))+"\n")

	#The median of CC
	f.write(str(np.median(list(cc.values())))+"\n")

	#The mean of CC
	f.write(str(np.mean(list(cc.values())))+"\n")

	#The standard deviation of CC
	f.write(str(np.std(list(cc.values())))+"\n")
		
	#The Degree Centrality of the graph
	dc = nx.centrality.degree_centrality(F)
				
	#The minimum of DC
	f.write(str(np.min(list(dc.values())))+"\n")

	#The maximum of DC
	f.write(str(np.max(list(dc.values())))+"\n")

	#The median of DC
	f.write(str(np.median(list(dc.values())))+"\n")

	#The mean of DC
	f.write(str(np.mean(list(dc.values())))+"\n")

	#The standard deviation of DC
	f.write(str(np.std(list(dc.values())))+"\n")
