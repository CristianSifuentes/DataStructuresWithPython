'''
Por supuesto, aquí tienes un ejemplo del algoritmo de ordenación por inserción en Python, junto con sus características, ventajas y desventajas.
'''
def ordenacion_por_insercion(lista):
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenación por inserción.
    
    Args:
    - lista: La lista que se desea ordenar.
    
    Returns:
    - La lista ordenada.
    """
    n = len(lista)
    for i in range(1, n):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = ordenacion_por_insercion(lista)
print("Lista ordenada:", lista_ordenada)

'''
Características y ventajas del algoritmo de ordenación por inserción:

Sencillez de implementación: El algoritmo de ordenación por inserción es fácil de entender e implementar.
Eficiencia en listas pequeñas o casi ordenadas: Es eficiente para listas pequeñas y casi ordenadas, ya que realiza un número mínimo de comparaciones y movimientos.
Estabilidad: Es estable, lo que significa que no cambia el orden relativo de elementos con claves iguales.
Desventajas:

Ineficiencia en listas grandes y desordenadas: Tiene una complejidad de tiempo de O(n^2), lo que lo hace ineficiente para listas grandes o desordenadas.
No es adecuado para listas enlazadas: No es adecuado para listas enlazadas debido a su naturaleza de intercambio de elementos contiguos.
Aunque el algoritmo de ordenación por inserción es útil para listas pequeñas o casi ordenadas, generalmente se prefieren otros algoritmos más rápidos como Quicksort o Merge Sort para listas más grandes o desordenadas. Es importante comprender las características y limitaciones de cada algoritmo de ordenación para seleccionar el más adecuado para cada situación
'''