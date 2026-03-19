"""
Crea un programa que lea una frase de la lista de invitados y cuente cuántas palabras comienzan con una vocal (a, e, i, o, u, sin distinción entre mayúsculas y minúsculas). A continuación, lee una lista de precios de entradas y calcula la suma de los dos últimos precios.

Imprime el recuento de vocales en la primera línea y la suma de los dos últimos precios en la segunda línea.
"""

# Lee la frase de lista de invitados.
sentence = input()

# Lee los precios de las entradas (números separados por espacios).
box_prices = []
while True:
    try:
        prices = float(input())
        box_prices.append(prices)
    except EOFError:
        break


# Pista: Divide la frase en palabras y comprueba la primera letra de cada palabra.


list_words = sentence.split(" ")
vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
vowel_count = 0
for i in list_words:
    if i.startswith(vocales):
        vowel_count += 1

print(vowel_count)
print(f"{box_prices[-2]+box_prices[-1]}")
# !TODO: Convierte la cadena de precios en una lista de números y suma los dos últimos..
# Pista: Divide los precios, conviértelos en números enteros y suma los dos úitmos elementos.


# Imprime los resultados.
