def quick_sort(lista):
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenación rápida (Quick Sort).
    
    Args:
    - lista: La lista que se desea ordenar.
    
    Returns:
    - La lista ordenada.
    """
    if len(lista) <= 1:
        return lista
    
    # Elegir un pivote
    pivote = lista[len(lista) // 2]
    
    # Dividir la lista en sublistas menores, mayores e iguales al pivote
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    # Llamar recursivamente a quick_sort para ordenar las sublistas menores y mayores
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)
