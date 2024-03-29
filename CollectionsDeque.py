'''
Claro, vamos a crear un ejemplo avanzado utilizando pilas implementadas con collections.deque. Supongamos que estamos construyendo un sistema de navegación para una aplicación, y queremos gestionar el historial de páginas visitadas.
'''

from collections import deque

# Definimos una pila (deque) para el historial de páginas visitadas
historial_paginas = deque(maxlen=5)  # Limitamos el historial a 5 páginas

# Función para simular la navegación a una página
def navegar_a_pagina(pagina):
    print(f"Navegando a la página: {pagina}")
    historial_paginas.append(pagina)  # Agregamos la página al historial

# Simulamos la navegación a varias páginas
navegar_a_pagina("Inicio")
navegar_a_pagina("Productos")
navegar_a_pagina("Ofertas")
navegar_a_pagina("Contacto")
navegar_a_pagina("Ayuda")
navegar_a_pagina("FAQ")
navegar_a_pagina("Soporte")

# Imprimimos el historial de páginas visitadas
print("Historial de páginas visitadas:")
for pagina in historial_paginas:
    print(pagina)

# Simulamos retroceder en el historial
pagina_retrocedida = historial_paginas.pop()
print(f"\nRetrocediendo a la página anterior: {pagina_retrocedida}")

# Imprimimos el historial actualizado
print("\nHistorial de páginas visitadas después de retroceder:")
for pagina in historial_paginas:
    print(pagina)


'''
En este ejemplo:

Utilizamos collections.deque para implementar una pila que representa el historial de páginas visitadas.
Limitamos el tamaño del historial a 5 páginas usando el argumento maxlen de deque.
Simulamos la navegación a diversas páginas y las agregamos al historial.
Mostramos el historial de páginas visitadas.
Simulamos retroceder en el historial utilizando el método pop de deque.
Este ejemplo ilustra cómo una pila implementada con collections.deque puede ser utilizada para gestionar el historial de una manera eficiente, y cómo se pueden aprovechar sus características, como el límite de tamaño automático, en el desarrollo diario de una aplicación.
'''