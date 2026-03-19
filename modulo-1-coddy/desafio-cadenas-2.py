"""
Escribe un programa que tome dos entradas:
    una cadena de texto y un carácter delimitador.
El programa debe dividir el texto por espacioes en blacno en palabras, luego unir estas palarbas usando el carácter delimitador especificado e imprimira la cadena resultante.
"""

text = input()
delimiter = input()


def delimitador(text, delimiter):
    new_list = text.split()
    print(delimiter.join(new_list))


delimitador(text, delimiter)
