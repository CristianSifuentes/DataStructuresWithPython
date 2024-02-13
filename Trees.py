'''
¡Claro! Los árboles son una estructura de datos no lineal que se utiliza comúnmente en informática para representar relaciones jerárquicas entre elementos. Son una herramienta poderosa y versátil que se utiliza en una variedad de aplicaciones, desde la representación de estructuras de datos en la memoria hasta la organización de datos en bases de datos y sistemas de archivos.

Voy a mostrarte un ejemplo de cómo implementar un árbol binario de búsqueda en Python. Este tipo de árbol tiene la ventaja de permitir búsquedas rápidas, inserciones eficientes y eliminaciones de elementos.
'''

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
        else:
            # Valor ya existe en el árbol, no hacemos nada
            pass

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        elif valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

# Creamos un árbol binario de búsqueda
arbol = ArbolBinarioBusqueda()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(18)

# Realizamos algunas búsquedas
print(arbol.buscar(7))  # True
print(arbol.buscar(11))  # False


'''
Características y ventajas de los árboles:

Eficiencia en búsquedas: La búsqueda en un árbol binario de búsqueda tiene complejidad de tiempo O(log n) en promedio.
Inserciones y eliminaciones eficientes: Las inserciones y eliminaciones también tienen complejidad de tiempo O(log n) en promedio.
Estructura jerárquica: Los árboles representan relaciones jerárquicas entre elementos, lo que los hace útiles para organizar y estructurar datos.
Desventajas:

Requiere balanceo: Si un árbol binario de búsqueda no está balanceado, puede degenerar en una estructura similar a una lista enlazada, lo que aumenta la complejidad de las operaciones.
Como programador, comprender y utilizar árboles te proporciona una herramienta poderosa para manejar y organizar datos de manera eficiente en una variedad de aplicaciones.
'''