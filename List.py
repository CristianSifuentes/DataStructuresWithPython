'''
¡Claro! Vamos a explorar un ejemplo más avanzado utilizando listas en Python. En este caso, crearemos un programa que realiza manipulación avanzada de datos utilizando comprensiones de listas, funciones lambda, y funciones de orden superior. Imaginemos que tenemos una lista de números y queremos realizar una serie de operaciones en ella.
'''

'''
Listas (list)

'''

# Generamos una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos una comprensión de lista para obtener el cuadrado de cada número
cuadrados = [x**2 for x in numeros]

# Filtramos solo los números pares usando una comprensión de lista con condición
numeros_pares = [x for x in numeros if x % 2 == 0]

# Aplicamos una función lambda para obtener la raíz cuadrada de cada número
raices_cuadradas = list(map(lambda x: x**0.5, numeros))

# Creamos una función de orden superior que toma una función como argumento
def operacion_personalizada(funcion, datos):
    return [funcion(x) for x in datos]

# Usamos la función de orden superior con una función personalizada
cubos = operacion_personalizada(lambda x: x**3, numeros)

# Imprimimos los resultados
print("Números originales:", numeros)
print("Cuadrados:", cuadrados)
print("Números pares:", numeros_pares)
print("Raíces cuadradas:", raices_cuadradas)
print("Cubos:", cubos)



'''
En este ejemplo:

Hacemos uso de comprensiones de listas para generar nuevas listas de manera concisa.
Utilizamos funciones lambda con map para aplicar una operación a cada elemento de la lista.
Definimos una función de orden superior llamada operacion_personalizada que toma una función como argumento y aplica esa función a cada elemento de la lista.
Este ejemplo demuestra algunos conceptos más avanzados de manipulación de listas en Python. La idea es mostrar cómo se pueden utilizar estas características para realizar operaciones más complejas y expresivas en los datos de una lista.

'''