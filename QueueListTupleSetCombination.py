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
