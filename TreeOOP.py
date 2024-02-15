'''
Por supuesto, aquí tienes un ejemplo avanzado que combina la programación orientada a objetos con el concepto de árboles. Vamos a implementar un árbol binario de búsqueda que permita agregar, buscar y eliminar nodos.
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

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._encontrar_minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo.valor

# Creamos un árbol binario de búsqueda
arbol = ArbolBinarioBusqueda()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(18)

# Realizamos algunas operaciones
print(arbol.buscar(7))  # True
arbol.eliminar(15)
print(arbol.buscar(15))  # False

'''
Características y ventajas:

Eficiencia en operaciones: Búsqueda, inserción y eliminación tienen complejidad de tiempo O(log n) en promedio.
Ordenamiento automático: Los árboles binarios de búsqueda mantienen sus elementos ordenados automáticamente.
Estructura jerárquica: La representación jerárquica de los datos es útil para una variedad de aplicaciones.
Desventajas:

Requiere balanceo: Si el árbol no está balanceado, las operaciones pueden volverse ineficientes.
Este ejemplo muestra cómo la programación orientada a objetos se puede utilizar para implementar una estructura de datos como un árbol binario de búsqueda. Al comprender y utilizar árboles de manera efectiva, puedes mejorar tu capacidad para manejar y organizar datos en tus proyectos.
'''
