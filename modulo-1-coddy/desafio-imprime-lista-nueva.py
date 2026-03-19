"""
Crea un programa que reciba una lista de números como entrada e imprima una nueva lista que:
    1. Contenga la lista original seguida de su reversa
    2. Tenga el primer elemento de la lista origianl insertado al principio y el último elemen to insertado al final
    3. Repita esta secuencia completa dos veces
"""

numbers = input().split()

step1 = numbers + numbers[::-1]
step2 = [numbers[0]] + step1 + [numbers[-1]]
step3 = step2 * 2
print(step3)
