'''
¡Por supuesto! Vamos a crear un ejemplo que combine collections.deque, listas, tuplas, diccionarios, conjuntos y queue.Queue. Imaginemos que estamos construyendo un sistema de gestión de tareas para un equipo de desarrollo y queremos utilizar diferentes estructuras de datos para manejar diferentes aspectos del proyecto.
'''

from collections import deque
import queue

# Definimos una cola para las tareas pendientes
cola_tareas = queue.Queue()

# Creamos una lista para almacenar tareas completadas
tareas_completadas = []

# Definimos una pila para el historial de tareas realizadas
historial_tareas = deque(maxlen=10)

# Creamos un diccionario para almacenar detalles de las tareas
detalles_tareas = {
    "Tarea1": {"responsable": "Alice", "prioridad": "Alta"},
    "Tarea2": {"responsable": "Bob", "prioridad": "Media"},
    "Tarea3": {"responsable": "Charlie", "prioridad": "Baja"}
}

# Creamos un conjunto para almacenar miembros del equipo
miembros_equipo = {"Alice", "Bob", "Charlie", "David", "Eve"}

# Simulamos la creación de algunas tareas y su asignación
for i in range(1, 4):
    tarea = f"Tarea{i}"
    responsable = detalles_tareas[tarea]["responsable"]
    if responsable in miembros_equipo:
        cola_tareas.put(tarea)  # Enqueue (Encolar) tareas pendientes

# Simulamos la ejecución de tareas
while not cola_tareas.empty():
    tarea_actual = cola_tareas.get()  # Dequeue (Desencolar) tarea
    # Realizamos la tarea y la movemos a la lista de tareas completadas
    tareas_completadas.append(tarea_actual)
    # Agregamos la tarea al historial
    historial_tareas.appendleft(tarea_actual)

# Imprimimos los resultados
print("Tareas completadas:", tareas_completadas)
print("\nHistorial de tareas realizadas:")
for tarea_realizada in historial_tareas:
    print(tarea_realizada)

print("\nDetalles de tareas:")
for tarea, detalles in detalles_tareas.items():
    print(f"{tarea}: Responsable - {detalles['responsable']}, Prioridad - {detalles['prioridad']}")

print("\nMiembros del equipo:", miembros_equipo)


'''
En este ejemplo:

Utilizamos queue.Queue para gestionar las tareas pendientes.
Utilizamos una lista para almacenar tareas completadas.
Utilizamos collections.deque para mantener un historial de las últimas tareas realizadas.
Utilizamos un diccionario para almacenar detalles específicos de cada tarea.
Utilizamos un conjunto para almacenar los miembros del equipo.
Esta combinación de estructuras de datos permite gestionar diferentes aspectos del proyecto, desde la cola de tareas pendientes hasta el historial de tareas realizadas y los detalles específicos de cada tarea. Estas estructuras pueden combinarse de manera eficiente para abordar diversos requisitos en un sistema de gestión de proyectos.
'''