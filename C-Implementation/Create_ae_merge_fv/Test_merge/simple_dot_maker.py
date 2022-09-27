import angr
import networkx as nx
from networkx.drawing.nx_pydot import write_dot

p = angr.Project('/home/nimda/Documents/ml-sample-pack-small/benign/arm/39eb154e0f0c2325e7c41989d24a54c85e34666076282a8614522c75ca3cff05', load_options={'auto_load_libs':False})
cfg = p.analyses.CFGFast()
write_dot(cfg.graph, 'file2.dot')

