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


grafo = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)], directed = True)

grafo.vs['label']=['A','B','C','D','E','F','G','H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]


plot(grafo, bbox = (300,300))

comunidades2 = grafo.clusters()
print(comunidades2)
comunidades2.membership

c = grafo.community_edge_betweenness()
print(c)
c.optimal_count

comunidades3 = c.as_clustering()
print(comunidades3)
comunidades3.membership
plot(grafo, bbox = (300,300), vertex_color = comunidades3.membership)

cores = comunidades3.membership

cores = np.array(cores)

cores = cores  * 100

cores = cores.tolist()

plot(grafo, bbox = (300,300), vertex_color = cores)

cli = grafo.as_undirected().cliques(min = 4)
print(cli)
len(cli)