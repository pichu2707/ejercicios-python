from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    price: str

def apply_discount(price:float, discount_pct: float )-> float:
    # BUG intenacional: si discoutn_pct viene como "20" en lugar de 0.20
    # el cálculo es incorrecto
    return price - (price * discount_pct)

def parse_discount(user_input:str)-> float:
    # El usuario introduce "20" para el 20%
    return float(user_input)

def total_cart(products: list[Product], discount_input: str) -> float:
    discount = parse_discount(discount_input)
    breakpoint() #Esto lo añadimos después y es desde la versión 3.7 de Python
    subtotal = sum(p.price for p in products)
    total = apply_discount(subtotal, discount)
    return round(total, 2)

def main():
    cart = [
            Product("A-001", 19.99),
            Product("B-002", 5.50),
            Product("C-003", 13.25),
            ]
    discount_input = "20" # el usuario cree que el 20%
    total = total_cart(cart, discount_input)
    print("Total: ", total)

if __name__=="__main__":
    main()
