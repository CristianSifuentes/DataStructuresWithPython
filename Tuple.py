''''

Claro, creemos un ejemplo avanzado que utiliza tuplas, métodos y características más avanzadas de Python. Supongamos que estamos gestionando información sobre empleados y sus salarios. Vamos a utilizar tuplas para representar la información y realizar algunas operaciones avanzadas.
'''

'''
Tuplas (tuple)

'''

# Definimos una lista de tuplas con información de empleados (nombre, salario base, horas extra)
empleados = [
    ("Alice", 50000, 10),
    ("Bob", 60000, 5),
    ("Charlie", 55000, 15),
    ("David", 70000, 8),
    ("Eve", 65000, 12)
]

# Función para calcular el salario total teniendo en cuenta las horas extra
def calcular_salario_total(empleado):
    nombre, salario_base, horas_extra = empleado
    tarifa_hora_extra = 1500  # Supongamos que la tarifa por hora extra es de 1500
    salario_total = salario_base + (horas_extra * tarifa_hora_extra)
    return nombre, salario_total

# Usamos una comprensión de tuplas para aplicar la función a cada empleado
salarios_totales = [calcular_salario_total(e) for e in empleados]

# Utilizamos la función sorted para ordenar la lista de salarios totales de manera descendente
salarios_ordenados = sorted(salarios_totales, key=lambda x: x[1], reverse=True)

# Imprimimos los resultados
print("Información de empleados:")
for empleado in empleados:
    print(empleado)

print("\nSalarios totales:")
for nombre, salario_total in salarios_ordenados:
    print(f"{nombre}: ${salario_total}")


'''
En este ejemplo:

* Hemos utilizado tuplas para representar la información de cada empleado, donde la tupla contiene el nombre, el salario base y las horas extra.
* Definimos una función calcular_salario_total que toma una tupla de empleado y devuelve una tupla con el nombre y el salario total, teniendo en cuenta las horas extra.
* Utilizamos una comprensión de tuplas para aplicar esta función a cada empleado y obtener una lista de salarios totales.
* Utilizamos la función sorted para ordenar la lista de salarios totales en orden descendente según los salarios.
* Finalmente, imprimimos la información original de los empleados y los salarios totales ordenados.
* Este ejemplo destaca el uso de tuplas, funciones, comprensiones de tuplas y la función sorted en un contexto más avanzado.
'''