'''

¡Claro! Vamos a combinar el uso de queue, listas, tuplas y conjuntos en un ejemplo. Supongamos que estamos creando un sistema de procesamiento de pedidos para una tienda en línea y queremos gestionar las órdenes utilizando diferentes estructuras de datos.
'''

import queue

# Definimos una cola para las órdenes
cola_ordenes = queue.Queue()

# Lista de productos disponibles en la tienda
productos_disponibles = ["Camiseta", "Pantalones", "Zapatos", "Sombrero", "Bufanda"]

# Tupla con los productos en oferta
productos_oferta = ("Bufanda", "Gorra", "Guantes")

# Conjunto de productos en liquidación
productos_liquidacion = {"Pantalones", "Sombrero", "Guantes"}

# Agregamos algunas órdenes a la cola
cola_ordenes.put(("Alice", {"Camiseta": 2, "Zapatos": 1}))
cola_ordenes.put(("Bob", {"Pantalones": 1, "Bufanda": 3}))
cola_ordenes.put(("Charlie", {"Sombrero": 2, "Gorra": 1}))

# Procesamos las órdenes
while not cola_ordenes.empty():
    nombre_cliente, productos_pedido = cola_ordenes.get()
    
    # Verificamos si hay productos en oferta en el pedido
    productos_oferta_en_pedido = set(productos_pedido.keys()) & set(productos_oferta)
    
    # Calculamos el total de la orden
    total_orden = sum(productos_pedido[producto] for producto in productos_pedido)
    
    # Aplicamos descuento del 10% si hay productos en liquidación en el pedido
    if set(productos_pedido.keys()) & productos_liquidacion:
        total_orden *= 0.9
    
    # Imprimimos la información de la orden procesada
    print(f"Cliente: {nombre_cliente}, Productos: {productos_pedido}, Total: ${total_orden:.2f}")
    
    # Enqueue (Encolar) tareas para el envío, por ejemplo, agregar a una lista de envío
    lista_envio = []
    for producto, cantidad in productos_pedido.items():
        lista_envio.extend([producto] * cantidad)
    
    print(f"Productos enviados: {lista_envio}\n")

# Resultado final
print("Productos disponibles en la tienda:", productos_disponibles)
print("Productos en oferta:", productos_oferta)
print("Productos en liquidación:", productos_liquidacion)

'''
En este ejemplo:

Utilizamos queue.Queue para gestionar las órdenes de los clientes.
Empleamos una lista para representar la lista de productos enviados para cada orden.
Utilizamos una tupla para definir los productos que están en oferta.
Utilizamos un conjunto para representar los productos en liquidación.
Realizamos operaciones como la intersección de conjuntos para verificar si hay productos en oferta en un pedido y aplicamos descuentos según los productos en liquidación.
Combinamos la información de diferentes estructuras de datos para procesar las órdenes de manera eficiente.
Este ejemplo ilustra cómo se pueden combinar diferentes estructuras de datos en un escenario práctico para gestionar y procesar pedidos en una tienda en línea.
'''
