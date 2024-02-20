'''
Por supuesto, aquí tienes un ejemplo avanzado que utiliza el algoritmo de búsqueda binaria para buscar un elemento en una lista ordenada. Vamos a explorar algunas de sus características, ventajas y desventajas.
'''

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


'''
Características y ventajas de la búsqueda binaria:

Eficiencia: La búsqueda binaria tiene una complejidad de tiempo O(log n), lo que la hace muy eficiente para listas ordenadas, especialmente para listas grandes.
Utiliza la ordenación: Aprovecha el hecho de que la lista está ordenada para realizar la búsqueda de manera eficiente.
Reducción del espacio de búsqueda: En cada iteración, reduce a la mitad el espacio de búsqueda, lo que permite encontrar el elemento en un número reducido de pasos.
Desventajas:

Requiere una lista ordenada: La lista debe estar ordenada previamente para que la búsqueda binaria funcione correctamente.
No es aplicable a listas no ordenadas: No se puede aplicar a listas no ordenadas, por lo que requiere un paso adicional de ordenación si la lista no está ordenada inicialmente.
La búsqueda binaria es una herramienta poderosa para buscar elementos en listas ordenadas de manera eficiente. Como programador, comprender sus características y aplicaciones te ayudará a tomar decisiones informadas sobre cuándo y cómo aplicarla en tus proyectos diarios.
'''

