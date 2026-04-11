def calculate_discount(price, discount_percentage):
    discount = round(price * (discount_percentage / 100), 2)
    return price - discount


print(calculate_discount(349.99, 25.5))
