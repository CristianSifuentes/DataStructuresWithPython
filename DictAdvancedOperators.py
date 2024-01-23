'''
¡Claro! Vamos a crear un ejemplo avanzado que destaque algunas características poderosas de los diccionarios en Python. 

Supongamos que estamos gestionando información sobre empleados en una empresa y queremos realizar operaciones avanzadas con los datos. 
Utilizaremos un diccionario para representar la información de cada empleado.

'''

# Diccionario con información de empleados (ID como clave y detalles como valor)
empleados = {
    101: {"nombre": "Alice", "salario": 60000, "departamento": "Ventas"},
    102: {"nombre": "Bob", "salario": 75000, "departamento": "Desarrollo"},
    103: {"nombre": "Charlie", "salario": 90000, "departamento": "Desarrollo"},
    104: {"nombre": "David", "salario": 70000, "departamento": "Recursos Humanos"},
    105: {"nombre": "Eve", "salario": 80000, "departamento": "Ventas"}
}

# Agregamos un nuevo empleado
empleados[106] = {"nombre": "Frank", "salario": 85000, "departamento": "Desarrollo"}

# Modificamos el salario de un empleado existente
empleados[101]["salario"] = 65000

# Eliminamos a un empleado
del empleados[105]

# Filtramos a los empleados del departamento de Desarrollo
empleados_desarrollo = {id_empleado: detalles for id_empleado, detalles in empleados.items() if detalles["departamento"] == "Desarrollo"}

# Ordenamos a los empleados por salario de mayor a menor
empleados_ordenados_por_salario = sorted(empleados.items(), key=lambda x: x[1]["salario"], reverse=True)

# Imprimimos los resultados
print("Información de empleados:")
for id_empleado, detalles in empleados.items():
    print(f"{id_empleado}: {detalles}")

print("\nEmpleados del departamento de Desarrollo:")
for id_empleado, detalles in empleados_desarrollo.items():
    print(f"{id_empleado}: {detalles}")

print("\nEmpleados ordenados por salario:")
for id_empleado, detalles in empleados_ordenados_por_salario:
    print(f"{id_empleado}: {detalles}")


'''
En este ejemplo:

Utilizamos un diccionario para representar la información de cada empleado, donde la clave es el ID del empleado y el valor es otro diccionario con detalles como el nombre, salario y departamento.
Agregamos un nuevo empleado, modificamos el salario de un empleado existente y eliminamos a otro empleado.
Utilizamos una comprensión de diccionario para filtrar a los empleados del departamento de Desarrollo.
Utilizamos sorted para ordenar a los empleados por salario de mayor a menor.
Este ejemplo resalta cómo los diccionarios en Python pueden ser eficientes y versátiles para gestionar información compleja y realizar operaciones avanzadas sobre los datos.

'''