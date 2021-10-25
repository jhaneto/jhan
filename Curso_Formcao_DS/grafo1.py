from igraph import Graph
from igraph import plot


grafo1 = Graph(edges = [(0,1),(1,2),(2,3),(3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount())
print(grafo1)
plot(grafo1, bbox = (300,300))



grafo2 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(0,3),(3,2),(2,1),(1,0)], directed = True)
grafo2.vs['label'] = range(grafo2.vcount())
print(grafo2)
plot(grafo2, bbox = (300,300))


grafo3 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(1,1)], directed = True)
grafo3.vs['label'] = range(grafo3.vcount())
print(grafo3)
plot(grafo3, bbox = (300,300))

grafo4 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(1,1)], directed = True)
grafo4.add_vertex(5)
grafo4.vs['label'] = range(grafo4.vcount())
print(grafo4)
plot(grafo4, bbox = (300,300))