"""
Escribe una función `update_inventory` que tome como parámetros `equipment_name`, `current_count` y `change_amount`, y devuelva una cadena con el inventario formateado.

La función actualiza el recuento de equipamiento sumando o restando la cantidad de cambio, y luego devuelve el resultado en un formato específico.

Parámetros:

equipment_name (str): Nombre del equipo de béisbol
current_count (int): Número actual de artículos en el inventario
change_amount (int): Cantidad a añadir (positiva) o a restar (negativa)
Devuelve: Cadena formateada que muestra el inventario actualizado. Formato: Equipment: [name] - Count: [updated_count]
"""

equipment_name = input()
current_count = int(input())
change_amount = int(input())


def update_inventory(equipment_name, current_count, change_amount):
    updated_count = current_count + change_amount
    print(f"Equipment: {equipment_name} - Count: {updated_count}")


update_inventory(equipment_name, current_count, change_amount)
