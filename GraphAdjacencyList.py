'''
Claro, aquí tienes un ejemplo avanzado que utiliza una lista de adyacencia para representar un grafo. Exploraremos algunas de sus características, ventajas y desventajas.
'''
class GrafoListaAdyacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adyacencia = [[] for _ in range(num_vertices)]

    def agregar_arista(self, origen, destino, peso=1):
        self.lista_adyacencia[origen].append((destino, peso))
        # Si el grafo es no dirigido, descomentar la siguiente línea
        # self.lista_adyacencia[destino].append((origen, peso))

    def mostrar(self):
        for i, adyacentes in enumerate(self.lista_adyacencia):
            print(f"Vértice {i}: {adyacentes}")

# Creamos un grafo utilizando una lista de adyacencia
grafo = GrafoListaAdyacencia(5)
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(4, 0)

# Mostramos la lista de adyacencia
print("Lista de adyacencia del grafo:")
grafo.mostrar()


'''
Características y ventajas de la lista de adyacencia:

Uso eficiente de memoria: La lista de adyacencia solo almacena información sobre las aristas que existen, por lo que es más eficiente en términos de memoria que una matriz de adyacencia, especialmente para grafos dispersos.
Flexibilidad en el almacenamiento de datos: Cada lista de adyacencia puede contener información adicional sobre las aristas, como pesos o capacidades.
Eficiencia en operaciones de modificación: Agregar o eliminar una arista es eficiente, generalmente O(1) o O(E), donde E es el número de aristas.
Desventajas:

Eficiencia en operaciones de consulta: La verificación de si existe una arista entre dos vértices puede requerir recorrer toda la lista de adyacencia correspondiente, lo que puede ser menos eficiente que en una matriz de adyacencia, especialmente para grafos densos.
Complejidad en operaciones de búsqueda: En grafos grandes, buscar una arista específica puede requerir recorrer todas las listas de adyacencia, lo que puede llevar a una complejidad de tiempo O(V + E), donde V es el número de vértices y E es el número de aristas.
La elección entre lista de adyacencia y matriz de adyacencia depende del tipo de grafo y del tipo de operaciones que se realizarán con él. La lista de adyacencia es adecuada para grafos dispersos o para operaciones frecuentes de modificación de aristas. Como programador, comprender las características y aplicaciones de las listas de adyacencia te ayudará a elegir la estructura de datos más adecuada para tus necesidades.
'''