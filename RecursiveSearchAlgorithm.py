'''

¡Genial! Aquí tienes un ejemplo avanzado que utiliza el algoritmo de búsqueda recursiva para buscar un elemento en una lista ordenada. Vamos a discutir algunas de sus características, ventajas y desventajas.
'''

def busqueda_binaria_recursiva(lista, elemento, izquierda, derecha):
    """
    Busca un elemento en una lista ordenada utilizando el algoritmo de búsqueda binaria de forma recursiva.
    
    Args:
    - lista: La lista ordenada en la que se realizará la búsqueda.
    - elemento: El elemento que se desea buscar.
    - izquierda: Índice izquierdo de la sublista actual.
    - derecha: Índice derecho de la sublista actual.
    
    Returns:
    - La posición del elemento en la lista si se encuentra, o -1 si no se encuentra.
    """
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    if lista[medio] == elemento:
        return medio
    elif lista[medio] < elemento:
        return busqueda_binaria_recursiva(lista, elemento, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, elemento, izquierda, medio - 1)

def busqueda_binaria(lista, elemento):
    """
    Función auxiliar para iniciar la búsqueda binaria de forma recursiva.
    """
    return busqueda_binaria_recursiva(lista, elemento, 0, len(lista) - 1)

# Creamos una lista de ejemplo ordenada
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Realizamos la búsqueda de un elemento en la lista
elemento = 13
posicion = busqueda_binaria(lista, elemento)
if posicion != -1:
    print(f"El elemento {elemento} está presente en la lista en la posición {posicion}.")
else:
    print(f"El elemento {elemento} no está presente en la lista.")


'''
Características y ventajas de la búsqueda binaria recursiva:

Eficiencia: La búsqueda binaria tiene una complejidad de tiempo O(log n), lo que la hace muy eficiente para listas ordenadas, especialmente para listas grandes.
Utiliza la ordenación: Aprovecha el hecho de que la lista está ordenada para realizar la búsqueda de manera eficiente.
Reducción del espacio de búsqueda: En cada iteración, reduce a la mitad el espacio de búsqueda, lo que permite encontrar el elemento en un número reducido de pasos.
Implementación concisa y elegante: La implementación recursiva puede ser más compacta y fácil de entender que su equivalente iterativo.
Desventajas:

Posible consumo de pila de recursión: Si la profundidad de la recursión es muy grande, puede consumir una cantidad significativa de memoria de pila.
La búsqueda binaria recursiva es una herramienta poderosa para buscar elementos en listas ordenadas de manera eficiente. Como programador, comprender sus características y aplicaciones te ayudará a tomar decisiones informadas sobre cuándo y cómo aplicarla en tus proyectos diarios.
'''