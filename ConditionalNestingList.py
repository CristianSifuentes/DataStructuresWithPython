# Lista de listas con productos y precios
productos_precios = [
    ["Laptop", 1200, False],
    ["Smartphone", 800, True],
    ["Tablet", 400, True],
    ["Cámara", 300, False],
    ["Auriculares", 100, True]
]

# Comprensión de lista anidada con condicionales
productos_con_descuento = [
    producto[0]  # Obtenemos el nombre del producto
    for producto in productos_precios  # Iteramos sobre cada lista de productos y precios
    if producto[1] > 500 and producto[2]  # Aplicamos condiciones: precio > 500 y descuento aplicado
]

# Imprimimos los resultados
print("Productos con descuento:", productos_con_descuento)
