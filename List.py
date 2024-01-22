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
