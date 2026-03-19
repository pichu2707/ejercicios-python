"""
Crea un programa que reciba una lista como entrada e imprima cuatro nuevas listas baasadas en las siguientes operaciones de slicing:
    1. Una lista que contenga cada cuarto elemento, comenzando desde el índice 2
    2. Una lista que contenga todos los elementos desde el 3er elemento hasta el 3er elemento desde el final.
    3. Una lista que contenga cada otro elemento en orden inverso, comenzando con el último elemento.
    4. Una lista que contenga los primeros tres y los últimos tres elementos de la lista original.
"""

original_list = input().split(",")
# 1 Lista que contenga cada cuatro elementos comenzando desde el 2
list1 = original_list[2::4]
# 2 Lista que contenga todos los elemtnos desde el 3er elemento hasta el 3er elemento final
list2 = original_list[2:-3]

# 3 Lista que contenga el orden inverso comenzando por el último elemento
list3 = original_list[::-2]

# 4 Lista que contenga los tres primeros y los tres últimos elementos de la lista original
lista_first = original_list[0:3]
lista_end = original_list[-3:]
list4 = lista_first + lista_end
# Resultados
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)
