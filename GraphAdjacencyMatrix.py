'''
Por supuesto, implementemos un ejemplo avanzado que utilice una matriz de adyacencia para representar un grafo y exploremos algunas de sus características, ventajas y desventajas.
'''

class GrafoMatrizAdyacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]

    def agregar_arista(self, origen, destino, peso=1):
        self.matriz[origen][destino] = peso
        # Si el grafo es no dirigido, descomentar la siguiente línea
        # self.matriz[destino][origen] = peso

    def mostrar(self):
        for fila in self.matriz:
            print(fila)

# Creamos un grafo utilizando una matriz de adyacencia
grafo = GrafoMatrizAdyacencia(5)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(4, 0)

# Mostramos la matriz de adyacencia
print("Matriz de adyacencia del grafo:")
grafo.mostrar()


'''
Características y ventajas de la matriz de adyacencia:

Representación directa de conexiones: Cada celda de la matriz indica si hay una conexión entre dos vértices.
Eficiencia en operaciones de consulta: La verificación de si existe una arista entre dos vértices es O(1).
Eficiencia en operaciones de modificación: Agregar o eliminar una arista es O(1).
Desventajas:

Uso de memoria: Una matriz de adyacencia utiliza una cantidad significativa de memoria, especialmente para grafos grandes o dispersos.
No adecuada para grafos grandes o dispersos: En grafos donde la mayoría de los vértices no están conectados entre sí, la matriz de adyacencia puede ser ineficiente en términos de uso de memoria.
La elección entre matriz de adyacencia y lista de adyacencia depende del tipo de grafo y de las operaciones que se realizarán con él. La matriz de adyacencia es adecuada para grafos densos o para operaciones frecuentes de consulta y modificación de conexiones. Como programador, comprender las características y aplicaciones de las matrices de adyacencia te ayudará a elegir la estructura de datos más adecuada para tus necesidades.
'''