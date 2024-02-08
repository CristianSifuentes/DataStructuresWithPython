'''
Claro, vamos a crear un ejemplo avanzado que implemente listas enlazadas, doblemente enlazadas y circulares en Python. Estas estructuras de datos son útiles para almacenar y manipular datos de manera eficiente, especialmente cuando el tamaño de la lista es grande o las operaciones de inserción y eliminación son frecuentes.

Primero, vamos a definir las clases para cada tipo de lista enlazada:
'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = nuevo_nodo
            self.primer_nodo = nuevo_nodo

    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo.siguiente = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo

    def eliminar(self, valor):
        nodo_actual = self.primer_nodo
        while nodo_actual:
            if nodo_actual.valor == valor:
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else:
                    self.primer_nodo = nodo_actual.siguiente

                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else:
                    self.ultimo_nodo = nodo_actual.anterior

                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def __str__(self):
        valores = []
        nodo_actual = self.primer_nodo
        while nodo_actual:
            valores.append(str(nodo_actual.valor))
            nodo_actual = nodo_actual.siguiente
        return " -> ".join(valores)

class ListaDobleEnlazada(ListaEnlazada):
    def insertar_al_final(self, valor):
        super().insertar_al_final(valor)

    def insertar_al_principio(self, valor):
        super().insertar_al_principio(valor)

    def eliminar(self, valor):
        super().eliminar(valor)

class ListaCircular(ListaEnlazada):
    def insertar_al_final(self, valor):
        super().insertar_al_final(valor)
        self.ultimo_nodo.siguiente = self.primer_nodo
        self.primer_nodo.anterior = self.ultimo_nodo

    def insertar_al_principio(self, valor):
        super().insertar_al_principio(valor)
        self.primer_nodo.anterior = self.ultimo_nodo
        self.ultimo_nodo.siguiente = self.primer_nodo

    def eliminar(self, valor):
        super().eliminar(valor)
        self.ultimo_nodo.siguiente = self.primer_nodo
        self.primer_nodo.anterior = self.ultimo_nodo


'''
Ahora, podemos crear instancias de cada tipo de lista, insertar, actualizar y eliminar datos, y mostrar el contenido de las listas:
'''

# Lista enlazada
print("Lista enlazada:")
lista_enlazada = ListaEnlazada()
lista_enlazada.insertar_al_principio(1)
lista_enlazada.insertar_al_principio(2)
lista_enlazada.insertar_al_final(3)
lista_enlazada.insertar_al_final(4)
print(lista_enlazada)

# Lista doblemente enlazada
print("\nLista doblemente enlazada:")
lista_doble_enlazada = ListaDobleEnlazada()
lista_doble_enlazada.insertar_al_principio(1)
lista_doble_enlazada.insertar_al_principio(2)
lista_doble_enlazada.insertar_al_final(3)
lista_doble_enlazada.insertar_al_final(4)
print(lista_doble_enlazada)

# Lista circular
print("\nLista circular:")
lista_circular = ListaCircular()
lista_circular.insertar_al_principio(1)
lista_circular.insertar_al_principio(2)
lista_circular.insertar_al_final(3)
lista_circular.insertar_al_final(4)
print(lista_circular)

# Eliminar un elemento de la lista doblemente enlazada
lista_doble_enlazada.eliminar(3)
print("\nLista doblemente")
