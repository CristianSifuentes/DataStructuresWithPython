# Conjunto de miembros del equipo del Proyecto A
equipo_proyecto_a = {"Alice", "Bob", "Charlie", "David", "Eve"}

# Conjunto de miembros del equipo del Proyecto B
equipo_proyecto_b = {"Bob", "Eve", "Frank", "Grace", "Hank"}

# Conjunto de miembros del equipo del Proyecto C
equipo_proyecto_c = {"Charlie", "David", "Eve", "Ivy", "Jack"}

# Encontramos el conjunto de todos los miembros del equipo
todos_los_empleados = equipo_proyecto_a.union(equipo_proyecto_b, equipo_proyecto_c)

# Encontramos el conjunto de empleados que trabajan en todos los proyectos
empleados_comunes = equipo_proyecto_a.intersection(equipo_proyecto_b, equipo_proyecto_c)

# Encontramos el conjunto de empleados que trabajan exclusivamente en el Proyecto A
empleados_proyecto_a_exclusivos = equipo_proyecto_a.difference(equipo_proyecto_b, equipo_proyecto_c)

# Comprobamos si el Proyecto A y el Proyecto B tienen algún miembro en común
proyectos_a_y_b_comparten_miembros = equipo_proyecto_a.isdisjoint(equipo_proyecto_b)

# Imprimimos los resultados
print("Todos los empleados:", todos_los_empleados)
print("Empleados comunes en todos los proyectos:", empleados_comunes)
print("Empleados exclusivos del Proyecto A:", empleados_proyecto_a_exclusivos)
print("¿Proyecto A y Proyecto B comparten miembros?", proyectos_a_y_b_comparten_miembros)
