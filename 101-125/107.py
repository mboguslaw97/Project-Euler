import networkx as nx
import numpy as np


def total_weight(G):
	return sum(G[e[0]][e[1]]['weight'] for e in G.edges())


file = open('107.txt')
adj = np.empty([40, 40])
for r, line in enumerate(file.readlines()):
	for c, x in enumerate(line.rstrip('\n').split(',')):
		adj[r, c] = 0 if x == '-' else int(x)

graph = nx.from_numpy_matrix(adj)
tree = nx.minimum_spanning_tree(graph)
print(total_weight(graph) - total_weight(tree))