"""
Crea una función llamada not_mutual_friends que tome dos listas de nombres representando las listas de amigos de dos personas. La función debe devolver una lista de nombres que son amigos solo de una persona (no amigos mutuos).

Vamos a decir que tenemos:

Amigos de la Persona A: ["John", "Emma", "Mike", "Sarah"]
Amigos de la Persona B: ["Emma", "Tom", "Sarah", "Peter"]
Cuando llamemos a not_mutual_friends con estas dos listas, debería devolver: ["John", "Mike", "Tom", "Peter"]

Explicación:

"John" y "Mike" son solo amigos de la Persona A
"Tom" y "Peter" son solo amigos de la Persona B
"Emma" y "Sarah" son amigos mutuos (amigos de ambas personas), por lo que no se incluyen en el resultado
"""

list1 = ["John", "Emma", "Mike", "Sarah"]
list2 = ["Emma", "Tom", "Sarah", "Peter"]


def not_mutual_friends(list1, list2):
    friends = []
    for i in list1:
        if i not in list2:
            friends.append(i)
    for i in list2:
        if i not in list1:
            friends.append(i)
    print(friends)


not_mutual_friends(list1, list2)
