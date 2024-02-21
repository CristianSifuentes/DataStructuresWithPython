def ordenacion_burbuja(lista):
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenación Burbuja.
    
    Args:
    - lista: La lista que se desea ordenar.
    
    Returns:
    - La lista ordenada.
    """
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = ordenacion_burbuja(lista)
print("Lista ordenada:", lista_ordenada)
