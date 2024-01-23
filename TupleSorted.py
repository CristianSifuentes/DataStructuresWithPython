# Lista de tuplas con información de estudiantes (nombre, calificaciones)
estudiantes = [
    ("Alice", {"Matemáticas": 90, "Historia": 85, "Inglés": 95}),
    ("Bob", {"Matemáticas": 88, "Historia": 92, "Inglés": 78}),
    ("Charlie", {"Matemáticas": 95, "Historia": 75, "Inglés": 88}),
    ("David", {"Matemáticas": 82, "Historia": 90, "Inglés": 85}),
    ("Eve", {"Matemáticas": 96, "Historia": 84, "Inglés": 92})
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
