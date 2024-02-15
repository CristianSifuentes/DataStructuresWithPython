'''
¡Claro! Los grafos son estructuras de datos que representan relaciones entre objetos. Son muy útiles para modelar una amplia gama de problemas del mundo real, como redes sociales, sistemas de navegación, planificación de rutas, entre otros. Implementemos un ejemplo avanzado que utilice grafos y discutamos algunas de sus características, ventajas y desventajas.
'''

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


'''
Características y ventajas de los grafos:

Flexibilidad: Los grafos pueden representar una amplia variedad de relaciones entre objetos.
Modelado de problemas complejos: Son útiles para modelar problemas del mundo real, como redes sociales, rutas de transporte, planificación de proyectos, etc.
Algoritmos eficientes: Existen algoritmos eficientes para resolver problemas en grafos, como el algoritmo de búsqueda en profundidad (DFS) y el algoritmo de búsqueda en anchura (BFS).
Reutilización de estructuras: Las estructuras de datos utilizadas para representar grafos (como listas de adyacencia o matrices de adyacencia) pueden reutilizarse en una variedad de algoritmos.
Desventajas:

Complejidad de implementación: La implementación de algoritmos y operaciones en grafos puede ser más compleja que en otras estructuras de datos.
Costo de almacenamiento: Dependiendo de la representación utilizada, los grafos pueden requerir más memoria que otras estructuras de datos.
El uso de grafos te permite abordar una variedad de problemas de manera eficiente y elegante. Al comprender los conceptos básicos y las operaciones en grafos, puedes mejorar tu capacidad para resolver problemas complejos en tus proyectos diarios.
'''