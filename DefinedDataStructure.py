class Cliente:
    def __init__(self, id_cliente, nombre, correo, puntos_fidelidad=0):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.puntos_fidelidad = puntos_fidelidad

    def __str__(self):
        return f"Cliente {self.id_cliente}: {self.nombre} ({self.correo}), Puntos de Fidelidad: {self.puntos_fidelidad}"


class RegistroClientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, cliente):
        if cliente.id_cliente not in self.clientes:
            self.clientes[cliente.id_cliente] = cliente
            print(f"Cliente {cliente.id_cliente} agregado al registro.")

    def buscar_cliente(self, id_cliente):
        return self.clientes.get(id_cliente, None)

    def actualizar_puntos_fidelidad(self, id_cliente, puntos):
        cliente = self.clientes.get(id_cliente, None)
        if cliente:
            cliente.puntos_fidelidad += puntos
            print(f"Se actualizaron los puntos de fidelidad para el cliente {id_cliente}.")

    def obtener_clientes_con_puntos_altos(self, puntos_minimos):
        return [cliente for cliente in self.clientes.values() if cliente.puntos_fidelidad >= puntos_minimos]


# Crear un registro de clientes y agregar algunos clientes
registro_clientes = RegistroClientes()

cliente1 = Cliente(1, "Alice", "alice@email.com", 100)
cliente2 = Cliente(2, "Bob", "bob@email.com", 150)
cliente3 = Cliente(3, "Charlie", "charlie@email.com", 120)

registro_clientes.agregar_cliente(cliente1)
registro_clientes.agregar_cliente(cliente2)
registro_clientes.agregar_cliente(cliente3)

# Buscar un cliente por ID
cliente_buscado = registro_clientes.buscar_cliente(2)
print("Cliente encontrado:", cliente_buscado)

# Actualizar puntos de fidelidad
registro_clientes.actualizar_puntos_fidelidad(1, 20)

# Obtener clientes con puntos de fidelidad altos
clientes_con_puntos_altos = registro_clientes.obtener_clientes_con_puntos_altos(130)
print("\nClientes con puntos de fidelidad altos:")
for cliente in clientes_con_puntos_altos:
    print(cliente)
