'''
Claro, aquí tienes un ejemplo avanzado que utiliza el algoritmo de búsqueda secuencial para buscar un elemento en una lista. Vamos a explorar algunas de sus características, ventajas y desventajas.
'''

def busqueda_secuencial(lista, elemento):
    """
    Busca un elemento en una lista utilizando el algoritmo de búsqueda secuencial.
    
    Args:
    - lista: La lista en la que se realizará la búsqueda.
    - elemento: El elemento que se desea buscar.
    
    Returns:
    - True si el elemento está presente en la lista, False en caso contrario.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

# Creamos una lista de ejemplo
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Realizamos la búsqueda de un elemento en la lista
elemento = 9
if busqueda_secuencial(lista, elemento):
    print(f"El elemento {elemento} está presente en la lista.")
else:
    print(f"El elemento {elemento} no está presente en la lista.")
    

'''
Características y ventajas de la búsqueda secuencial:

Sencillez: Es un algoritmo simple de implementar y entender.
Flexibilidad: Puede aplicarse a cualquier tipo de lista, no requiere que esté ordenada.
Eficiencia en listas pequeñas: Es eficiente para listas pequeñas o cuando el elemento buscado está cerca del principio de la lista.
Desventajas:

Ineficiencia en listas grandes: La búsqueda secuencial tiene una complejidad de tiempo O(n), lo que significa que puede volverse ineficiente para listas grandes, ya que debe recorrer todos los elementos en el peor de los casos.
No aprovecha la ordenación: No se beneficia de la ordenación de la lista, por lo que puede ser menos eficiente que otros algoritmos de búsqueda en listas ordenadas.
La búsqueda secuencial es útil cuando se trabaja con listas pequeñas o cuando la lista no está ordenada. Sin embargo, para listas grandes o cuando se necesita una mayor eficiencia, pueden ser más adecuados otros algoritmos de búsqueda, como la búsqueda binaria en listas ordenadas. Como programador, es importante comprender las características y aplicaciones de cada algoritmo de búsqueda para elegir el más adecuado según el contexto del problema.
'''
