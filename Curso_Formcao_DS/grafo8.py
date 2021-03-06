from igraph import Graph
from igraph import plot
import igraph
import numpy as np

grafo = igraph.load('Grafo.graphml')
print(grafo)

plot(grafo, bbox = (300,300))

comunidades = grafo.clusters()
print(comunidades)

comunidades.membership

plot(grafo, vertex_color = comunidades.membership)

grafo2 = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)], directed = True)

grafo2.vs['label']=['A','B','C','D','E','F','G','H']
grafo2.es['weight'] = [2,1,2,1,2,1,3,1]

igraph.plot(grafo2, bbox = (300,300), edge_label = grafo.es['weight']).show()

c = grafo2.community_edge_betweenness()
print(c)

comunidades3 = c.as_clustering()
print(comunidades3)
comunidades3.membership

igraph.plot(grafo2, bbox = (300,300), edge_label = grafo.es['weight']).show()
cores = comunidades3.membership
cores = np.array(cores)
cores = cores * 100
cores = cores.tolist()
plot(grafo2, vertex_color = cores).show()

cli = grafo.as_undirected().cliques(min = 4)
print(cli)
len(cli)