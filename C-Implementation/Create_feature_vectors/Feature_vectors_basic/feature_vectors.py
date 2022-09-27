import sys
import angr
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p = angr.Project('/home/nimda/Documents/ml-sample-pack-small/benign/arm/3ab1aba951f870d389c8fed8c4fd1672128b06c2e8cbef49ae689b01907a5318', load_options={'auto_load_libs':False})

cfg = p.analyses.CFGFast()

G = cfg.graph

with open('test2.txt', 'w') as f:

    sys.stdout = f
    
    #Number of edges in the graph
    print(str(nx.number_of_edges(G)))

    #Number of nodes in the graph
    print(nx.number_of_nodes(G))

    #The density of a graph
    print(nx.density(G))
    
    #The number of components
    print(nx.number_weakly_connected_components(G))
    
#----------------------SPL START----------------------------

    #The shortest path length
    sp = dict(nx.all_pairs_shortest_path_length(G))
    #print(sp)

    #The minimum of shortest path
    df =  [np.min(list(spl.values())) for spl in sp.values()]
    mindf = np.min(df)
    print("The minimum for shortest path: ")
    print(mindf)
    
    #The maximum of shortest path
    df =  [np.min(list(spl.values())) for spl in sp.values()]
    maxdf = np.max(df)
    print("The maximum for shortest path: ")
    print(maxdf)
    
    #The median of shortest path
    df = []
    for spl in sp.values():
    	df += spl.values()
    medf = np.median(df)
    print("The median for shortest path: ")
    print(medf)
    
    #The mean of shortest path
    df = []
    for spl in sp.values():
    	df += spl.values()
    meandf = np.mean(df)
    print("The mean for shortest path: ")
    print(meandf) 
    
    #The standard deviation of shortest path
    df = []
    for spl in sp.values():
    	df += spl.values()
    stdf = np.std(df)
    print("The std for shortest path: ")
    print(stdf)
    
#----------------------BETWEENNESS START----------------------------
        
    #The Betweenness Centrality of the graph
    bc = dict(nx.centrality.betweenness_centrality(G))
    #print(bc)

    #The minimum of BC
    print(np.min(list(bc.values())))
    print("The minimum of BC: ")
    
    #The maximum of BC
    maxdf = np.max(list(bc.values()))
    print("The maximum of BC: ")
    print(maxdf)
    
    #The median of BC
    medf = np.median(list(bc.values()))
    print("The median of BC: ")
    print(medf)
    
    #The mean of BC
    meandf = np.mean(list(bc.values()))
    print("The mean of BC: ")
    print(meandf) 
    
    #The standard deviation of BC
    stdf = np.std(list(bc.values()))
    print("The std of BC: ")
    print(stdf)
    
 #----------------------CLOSENESS START----------------------------
        
    #The Closeness Centrality of the graph
    cc = nx.centrality.closeness_centrality(G)
    
    #The minimum of CC
    mindf = np.min(list(cc.values()))
    print("The minimum of CC: ")
    
    #The maximum of CC
    maxdf = np.max(list(cc.values()))
    print("The maximum of CC: ")
    print(maxdf)
    
    #The median of CC
    medf = np.median(list(cc.values()))
    print("The median of CC: ")
    print(medf)
    
    #The mean of CC
    meandf = np.mean(list(cc.values()))
    print("The mean of CC: ")
    print(meandf) 
    
    #The standard deviation of CC
    stdf = np.std(list(cc.values()))
    print("The std of CC: ")
    print(stdf)

#----------------------CLOSENESS START----------------------------

    #The Degree Centrality of the graph
    dc = nx.centrality.degree_centrality(G)
    
    #The minimum of DC
    mindf = np.min(list(dc.values()))
    print("The minimum of DC: ")
    
    #The maximum of DC
    maxdf = np.max(list(dc.values()))
    print("The maximum of DC: ")
    print(maxdf)
    
    #The median of DC
    medf = np.median(list(dc.values()))
    print("The median of DC: ")
    print(medf)
    
    #The mean of DC
    meandf = np.mean(list(dc.values()))
    print("The mean of DC: ")
    print(meandf) 
    
    #The standard deviation of DC
    stdf = np.std(list(dc.values()))
    print("The std of DC: ")
    print(stdf)
    
