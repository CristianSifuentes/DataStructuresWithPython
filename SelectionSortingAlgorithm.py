'''
Por supuesto, aquí tienes un ejemplo del algoritmo de ordenación por selección en Python, junto con sus características, ventajas y desventajas.
'''
def ordenacion_por_seleccion(lista):
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenación por selección.
    
    Args:
    - lista: La lista que se desea ordenar.
    
    Returns:
    - La lista ordenada.
    """
    n = len(lista)
    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = ordenacion_por_seleccion(lista)
print("Lista ordenada:", lista_ordenada)


'''
Características y ventajas del algoritmo de ordenación por selección:

Sencillez de implementación: El algoritmo de ordenación por selección es fácil de entender e implementar.
Eficiencia en listas pequeñas: Es eficiente para listas pequeñas debido a su naturaleza de búsqueda del mínimo en cada iteración.
Estabilidad: Es estable, lo que significa que no cambia el orden relativo de elementos con claves iguales.
Desventajas:

Ineficiencia en listas grandes: Tiene una complejidad de tiempo de O(n^2), lo que lo hace ineficiente para listas grandes o casi ordenadas.
No es adecuado para listas enlazadas: No es adecuado para listas enlazadas debido a su naturaleza de intercambio de elementos contiguos.
Aunque el algoritmo de ordenación por selección es útil para listas pequeñas o en situaciones donde la simplicidad es más importante que la eficiencia, generalmente se prefieren otros algoritmos más rápidos para listas más grandes. Es importante comprender las características y limitaciones de cada algoritmo de ordenación para seleccionar el más adecuado para cada situación.
'''