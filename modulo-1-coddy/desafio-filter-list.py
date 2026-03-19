# Crea un programa que reciba dos listas e imprima una nueva lista con todos los elementos que están en la primera lista pero NO en la segunda.


lst1 = input().split(",")
lst2 = input().split(",")


def filterList(lst1, lst2):
    final_list = []
    for i in lst1:
        if i in lst1 and i not in lst2:
            final_list.append(i)
    print(final_list)


filterList(lst1, lst2)
