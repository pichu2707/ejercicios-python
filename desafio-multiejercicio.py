# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
# Your code here
for i in range(30, 81):
    if i % 4 == 0:
        print(i, end=", ")
print()  # Creates a new line for better readability

# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
# Your code here
for i in range(1, 30):
    if i % 2 == 1 and i >= 15:
        print(i, end=", ")
print()  # Creates a new line for better readability

# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
# Your code here
for i in range(50, 9, -1):
    if i % 5 == 0:
        print(i, end=", ")
print()  # Creates a new line for better readability

# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")

# Your code here
result = 1
for i in range(1, 31):
    if i % 3 == 0:
        result *= i

print(result)


# Remember: print only the number, not "Product = number"
