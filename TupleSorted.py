'''

Claro, creemos un ejemplo más avanzado que involucre tuplas, sorted, condicionales y expresiones avanzadas de selección. Supongamos que estamos gestionando información sobre estudiantes y sus calificaciones en diferentes asignaturas, y queremos realizar operaciones avanzadas de selección y ordenamiento.

'''


# Lista de tuplas con información de estudiantes (nombre, calificaciones)
estudiantes = [
    ("Alice", {"Matemáticas": 100, "Historia": 100, "Inglés": 95}),
    ("Bob", {"Matemáticas": 88, "Historia": 92, "Inglés": 78}),
    ("Charlie", {"Matemáticas": 95, "Historia": 75, "Inglés": 88}),
    ("David", {"Matemáticas": 82, "Historia": 90, "Inglés": 85}),
    ("Eve", {"Matemáticas": 96, "Historia": 94, "Inglés": 92})
]

# Seleccionamos a los estudiantes que tienen un promedio superior a 90 en todas las asignaturas
estudiantes_destacados = [
    (nombre, calificaciones)
    for nombre, calificaciones in estudiantes
    if all(calificacion > 90 for calificacion in calificaciones.values())
]

# Ordenamos a los estudiantes destacados por el promedio general de sus calificaciones
estudiantes_destacados_ordenados = sorted(
    estudiantes_destacados,
    key=lambda x: sum(x[1].values()) / len(x[1]),
    reverse=True
)

# Imprimimos los resultados
print("Información de estudiantes:")
for nombre, calificaciones in estudiantes:
    print(f"{nombre}: {calificaciones}")

print("\nEstudiantes destacados:")
for nombre, calificaciones in estudiantes_destacados_ordenados:
    promedio_general = sum(calificaciones.values()) / len(calificaciones)
    print(f"{nombre}: Promedio general {promedio_general:.2f}")


'''
En este ejemplo:

Utilizamos una lista de tuplas, donde cada tupla contiene el nombre de un estudiante y un diccionario de calificaciones en diferentes asignaturas.
Utilizamos una comprensión de lista para seleccionar a los estudiantes que tienen un promedio superior a 90 en todas las asignaturas.
Utilizamos sorted para ordenar a los estudiantes destacados por su promedio general, calculado con una expresión lambda.
Imprimimos la información original de los estudiantes y luego la información de los estudiantes destacados ordenada por promedio general.
Este ejemplo destaca el uso de tuplas, expresiones avanzadas de selección, y ordenamiento con sorted en un contexto más avanzado.

'''
