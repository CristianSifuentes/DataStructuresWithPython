import queue
import threading
import time

# Función que simula una tarea de procesamiento
def procesar_tarea(tarea):
    print(f"Procesando tarea: {tarea}")
    time.sleep(2)  # Simulamos un tiempo de procesamiento

# Clase que representa un trabajador (thread) que toma tareas de la cola y las procesa
class Trabajador(threading.Thread):
    def __init__(self, nombre, cola):
        super().__init__()
        self.nombre = nombre
        self.cola = cola

    def run(self):
        while True:
            tarea = self.cola.get()  # Obtenemos una tarea de la cola
            if tarea is None:
                break  # Si recibimos None, terminamos el hilo
            procesar_tarea(tarea)
            self.cola.task_done()  # Indicamos que la tarea se ha completado

# Creamos una cola para gestionar tareas
cola_tareas = queue.Queue()

# Creamos varios trabajadores que toman tareas de la cola y las procesan
trabajador_1 = Trabajador("Trabajador 1", cola_tareas)
trabajador_2 = Trabajador("Trabajador 2", cola_tareas)

# Iniciamos los trabajadores
trabajador_1.start()
trabajador_2.start()

# Enqueue (Encolar) tareas
for i in range(1, 6):
    tarea = f"Tarea-{i}"
    cola_tareas.put(tarea)

# Esperamos a que todas las tareas se completen
cola_tareas.join()

# Detenemos los trabajadores después de completar todas las tareas
cola_tareas.put(None)
cola_tareas.put(None)
trabajador_1.join()
trabajador_2.join()

print("Todas las tareas han sido procesadas.")

'''
En este ejemplo:

Utilizamos queue.Queue para crear una cola que maneja tareas de procesamiento.
Creamos una clase Trabajador que representa un hilo que toma tareas de la cola y las procesa.
Envolvemos el procesamiento de tareas en un hilo para simular la ejecución asíncrona.
Utilizamos métodos como put, get, y task_done para gestionar la cola de manera segura entre hilos.
Utilizamos join para esperar a que todas las tareas se completen antes de finalizar el programa.
Este ejemplo resalta cómo queue.Queue puede ser utilizado para coordinar eficientemente el trabajo entre múltiples hilos, un escenario común en programación asíncrona y concurrente.
'''