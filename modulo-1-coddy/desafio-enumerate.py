# Dada una lsita separada por comas de números como entrada, i preme una lista de los índices de números que cumplan cualquiera de las siguientes condiciones:
# * El número es menor que 50
# *  EL número es divisible por 5 (el resto es 0 cuando se divide por 5)

lst = list(map(int, input().split(",")))


def listado(lst):
    lista = []
    for i, num in enumerate(lst):
        if num < 50 or num % 5 == 0:
            lista.append(i)
    print(lista)


listado(lst)
