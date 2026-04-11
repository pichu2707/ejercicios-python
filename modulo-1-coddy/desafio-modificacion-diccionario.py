"""
Crea una función llamada `update_employee_info` que toma tres paramétros:
    `employee_dict` (un diccionario), `key` (una cadena), y `value`.
La función debe actualizar el `employee_dict` con a nueva key y value. Si lla clave ya existe, su valor debe actualizarse. Si lla clave no existe se debe agregar un nuevo par clave-valor. La función debe devolver el diccionario actualizado.

Importante: Asegúrate de modificar el diccionario original y devolverlo,. Usa la notacion d ecorchetes dict['key'] = value para agregar o actualizar entradas.
"""


def update_employee_info(employee_dict, key, value):
    employee_dict[key] = value
    return employee_dict


print(
    update_employee_info(
        {"name": "Alice", "age": 30, "departament": "HR"}, "city", "New York"
    )
)
