'''
¡Por supuesto! Vamos a crear un ejemplo avanzado de comprensión de listas en Python que involucra anidamiento, condicionales y una operación más compleja. Supongamos que tenemos una lista de listas que representan productos y sus precios, y queremos obtener una lista con los nombres de los productos que tienen un descuento aplicado.
'''


# Lista de listas con productos y precios
productos_precios = [
    ["Laptop", 1200, False, False, 'C'],
    ["Smartphone", 800, True, True, 'C'],
    ["Tablet", 400, True, True,  'C'],
    ["Cámara", 300, False, False, 'C'],
    ["Auriculares", 100, True, False, 'C'],
    ["Sofa", 100, True, False, 'M'],
    ["Cama", 100, True, False, 'M']
]

# Comprensión de lista anidada con condicionales
productos_con_descuento = [
    producto[0]  # Obtenemos el nombre del producto
    for producto in productos_precios  # Iteramos sobre cada lista de productos y precios
    if producto[1] > 500 and producto[2]  # Aplicamos condiciones: precio > 500 y descuento aplicado
]

productos_en_existencia = [
    producto[0]
    for producto in productos_precios
    if producto[3] == True 
]


# Imprimimos los resultados
print("Productos con descuento:", productos_con_descuento)
print("Productos en existencia:", productos_en_existencia)


'''
En este ejemplo:

Utilizamos una comprensión de lista anidada para iterar sobre la lista de listas productos_precios.
Aplicamos un condicional (if) para seleccionar solo los productos que tienen un precio superior a 500 y que tienen un descuento aplicado (tercer elemento de la sublista).
La expresión producto[0] nos da el nombre del producto, y eso es lo que se incluye en la nueva lista.
Este ejemplo muestra cómo se pueden combinar anidamiento, condicionales y operaciones más complejas en una sola comprensión de lista para filtrar y transformar datos de manera eficiente y expresiva.
'''