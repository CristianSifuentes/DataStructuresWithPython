def busqueda_binaria(lista, elemento):
    """
    Busca un elemento en una lista ordenada utilizando el algoritmo de búsqueda binaria.
    
    Args:
    - lista: La lista ordenada en la que se realizará la búsqueda.
    - elemento: El elemento que se desea buscar.
    
    Returns:
    - La posición del elemento en la lista si se encuentra, o -1 si no se encuentra.
    """
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Creamos una lista de ejemplo ordenada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Realizamos la búsqueda de un elemento en la lista
elemento = 5
posicion = busqueda_binaria(lista, elemento)
if posicion != -1:
    print(f"El elemento {elemento} está presente en la lista en la posición {posicion}.")
else:
    print(f"El elemento {elemento} no está presente en la lista.")
