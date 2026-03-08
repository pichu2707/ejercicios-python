print("Welcome to FizzBuzz!")
n = int(input())


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            print("FizzBuzz")
        elif i % 7 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif "3" in str(i):
            print("Almost Fizz")
        else:
            print(i)


fizzbuzz(n)
