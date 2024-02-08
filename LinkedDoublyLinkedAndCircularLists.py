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
