"""
Crea un programa que ayude a realizar un seguimiento de las recompensas por fidelidad de una empresa de mudanzas.
Lee el importe total de la compra y calcula los puntos de fidelidad (1 punto por cada 10 $ gastados, redondeando hacia abajo).
A continuación, lee un índice inicial y una lista de etiquetas de cajas, e imprime los puntos seguidos de todas las cajas desde ese índice hasta el final.
"""

# Read the total purchase amount
purchase_amount = float(input())

# Calculate loyalty points (1 point per $10 spent, rounded down)
points = int(purchase_amount // 10)

# Read the starting index
start_index = int(input())

# Read box labels until there is no more input
box_labels = []

while True:
    try:
        box = input()
        box_labels.append(box)
    except EOFError:
        break

# Print loyalty points
print(points)

# Print boxes from start_index to the end
for box in box_labels[start_index:]:
    print(box)
