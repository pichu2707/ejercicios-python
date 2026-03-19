# Cada caso de prueba tiene unaentrada: un impar número entero ( siempre impar, dado)
# Piramide n usando *

n = int(input())

if n % 2 == 1 and n <= 1000:
    for i in range(1, n + 1, 2):
        print("*" * i)
