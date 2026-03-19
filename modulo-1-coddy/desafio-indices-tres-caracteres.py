lst = input().split()
lista = []
for indice, elemento in enumerate(lst):
    if elemento.startswith("a") or len(elemento) > 3:
        lista.append(indice)
print(lista)
