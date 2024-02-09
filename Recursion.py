from collections import deque

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

# Creamos una cola para las tareas pendientes
cola_tareas = deque()

def agregar_tarea(descripcion):
    nueva_tarea = Tarea(descripcion)
    cola_tareas.append(nueva_tarea)
    print(f"Tarea agregada: {nueva_tarea}")

def imprimir_tareas_pendientes(cola):
    if cola:
        tarea = cola.popleft()
        print(f"Tarea pendiente: {tarea}")
        imprimir_tareas_pendientes(cola)
        cola.appendleft(tarea)

# Simulamos el uso del sistema de gestión de tareas
agregar_tarea("Hacer la compra")
agregar_tarea("Preparar informe")
agregar_tarea("Llamar al cliente")

# Imprimimos las tareas pendientes utilizando recursividad
print("\nTareas pendientes:")
imprimir_tareas_pendientes(cola_tareas)
