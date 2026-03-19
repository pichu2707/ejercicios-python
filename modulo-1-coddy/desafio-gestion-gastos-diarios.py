print("Welcome to the Daily Expense Tracker!\n")

print(
    """Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit"""
)
choices = [1, 2, 3, 4, 5]
gastos = []
choice = 0
expenses = 0
average = 0
while choice != 5:
    choice = int(input())
    if choice == 1:
        precio = float(input())
        gastos.append(precio)
        print("Expense added successfully!")
    if choice == 2:
        if len(gastos) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for indice, valor in enumerate(gastos):
                print(f"{indice+1}. {valor}")
    if choice == 3:
        if len(gastos) == 0:
            print("No expenses recorded yet.")
        else:
            for i in gastos:
                expenses = expenses + i
                average = expenses / (len(gastos))
            print(f"Total expense: {float(expenses)}")
            print(f"Average expense: {float(average)}")
    if choice == 4:
        gastos.clear()
        print("All expenses cleared.")
    if choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
    if choice not in choices:
        print("Invalid choice. Please try again.")
