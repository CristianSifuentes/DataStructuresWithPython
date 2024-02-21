'''
Claro, aquí tienes un ejemplo de cómo implementar el algoritmo de ordenación mezcla (Merge Sort) en Python, junto con algunas características, ventajas y desventajas:
'''
def merge_sort(lista):
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenación mezcla (Merge Sort).
    
    Args:
    - lista: La lista que se desea ordenar.
    
    Returns:
    - La lista ordenada.
    """
    if len(lista) <= 1:
        return lista
    
    # Dividir la lista en mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    # Llamar recursivamente a merge_sort para ordenar las mitades
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    
    # Mezclar las mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    """
    Mezcla dos listas ordenadas en una lista ordenada.
    
    Args:
    - izquierda: La lista izquierda.
    - derecha: La lista derecha.
    
    Returns:
    - La lista mezclada y ordenada.
    """
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregar los elementos restantes de la lista izquierda
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1
    
    # Agregar los elementos restantes de la lista derecha
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1
    
    return resultado

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)


'''
Características y ventajas del algoritmo de ordenación mezcla (Merge Sort):

Eficiencia: Tiene un tiempo de ejecución garantizado de O(n log n), lo que lo hace muy eficiente, especialmente para listas grandes.
Estabilidad: Es estable, lo que significa que no cambia el orden relativo de elementos con claves iguales.
No requiere memoria adicional: No requiere memoria adicional aparte de la necesaria para la lista original.
Desventajas:

Uso de memoria: Requiere memoria adicional para almacenar las sublistas durante el proceso de mezcla.
No es in-place: Requiere espacio adicional para almacenar las sublistas, lo que puede ser problemático para listas muy grandes debido a la fragmentación de la memoria.
En resumen, el algoritmo de ordenación mezcla (Merge Sort) es una opción muy eficiente y estable para ordenar listas, especialmente cuando se trata de listas grandes. Sin embargo, puede requerir más memoria que otros algoritmos y no es in-place.
'''
