from collections import defaultdict

class Grafo:
    def __init__(self):
        self.vertices = defaultdict(list)

    def agregar_arista(self, u, v):
        self.vertices[u].append(v)

    def dfs(self, inicio, visitado=None):
        if visitado is None:
            visitado = set()
        visitado.add(inicio)
        print(inicio, end=' ')
        for vecino in self.vertices[inicio]:
            if vecino not in visitado:
                self.dfs(vecino, visitado)

# Creamos un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

# Realizamos un recorrido DFS (Depth-First Search) en el grafo
print("Recorrido DFS desde el vértice 2:")
grafo.dfs(2)
