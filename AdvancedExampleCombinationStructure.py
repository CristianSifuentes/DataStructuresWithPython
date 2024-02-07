from collections import deque
import queue

class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad_disponible):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio}, Disponibles: {self.cantidad_disponible}"

class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} ({self.correo})"

class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto.id_producto in self.productos:
            self.productos[producto.id_producto] += cantidad
        else:
            self.productos[producto.id_producto] = cantidad

    def __str__(self):
        return f"Pedido {self.id_pedido} - Cliente: {self.cliente.nombre}, Productos: {len(self.productos)}"

# Creamos algunos productos
producto1 = Producto(1, "Camiseta", 20, 50)
producto2 = Producto(2, "Pantalones", 30, 40)
producto3 = Producto(3, "Zapatos", 50, 30)

# Creamos un registro de clientes y agregamos algunos clientes
registro_clientes = {
    1: Cliente(1, "Alice", "alice@email.com"),
    2: Cliente(2, "Bob", "bob@email.com")
}

# Creamos una cola para los pedidos
cola_pedidos = queue.Queue()

# Creamos un inventario de productos
inventario_productos = {
    producto1.id_producto: producto1,
    producto2.id_producto: producto2,
    producto3.id_producto: producto3
}

# Simulamos la creación de algunos pedidos
pedido1 = Pedido(1, registro_clientes[1])
pedido1.agregar_producto(producto1, 2)
pedido1.agregar_producto(producto2, 1)

pedido2 = Pedido(2, registro_clientes[2])
pedido2.agregar_producto(producto3, 3)

# Encolamos los pedidos
cola_pedidos.put(pedido1)
cola_pedidos.put(pedido2)

# Procesamos los pedidos
while not cola_pedidos.empty():
    pedido_actual = cola_pedidos.get()
    print(f"Procesando {pedido_actual}...")

    for id_producto, cantidad in pedido_actual.productos.items():
        producto = inventario_productos.get(id_producto)
        if producto and producto.cantidad_disponible >= cantidad:
            producto.cantidad_disponible -= cantidad
            print(f"Producto {producto.nombre}: {cantidad} unidades vendidas.")
        else:
            print(f"No hay suficientes unidades disponibles de {producto.nombre}.")

    print()

# Actualizamos el inventario después de procesar los pedidos
print("Inventario actualizado:")
for producto in inventario_productos.values():
    print(producto)
