"""
Crea una función llamada find_occurrences que:

Toma dos argumentos de cadena: text y pattern
Cuenta cuántas veces aparece pattern en text, incluyendo ocurrencias superpuestas
Devuelve una tupla que contiene:
Un booleano que indica si se encontró el patrón (True/False)
El número de ocurrencias del patrón
Una lista de posiciones iniciales donde se encontró el patrón
Por ejemplo, si text es "abababab" y pattern es "aba", tu función debería devolver (True, 3, [0, 2, 4]), ya que "aba" aparece en las posiciones 0, 2 y 4.

Si no se encuentra el patrón, devuelve (False, 0, []).

Acerca de la pass palabra clave: Verás pass en el código predeterminado. Es una palabra clave de Python que significa "no hacer nada" y se usa como marcador de posición cuando Python requiere un bloque de código indentado (como dentro de una función). Deberías reemplazar pass con tu código de función real.
"""


def find_occurrences(text, pattern):
    count = 0
    position = []
    for i in range(len(text) - len(pattern) + 1):
        fragment = text[i : i + len(pattern)]
        if fragment == pattern:
            count += 1
            position.append(i)

    if count > 0:
        return (True, count, position)
    else:
        return (False, count, position)


# Leyendo entradas
text = input()
pattern = input()

# LLamada a la función y  pintar el resultado
result = find_occurrences(text, pattern)
print(result)
