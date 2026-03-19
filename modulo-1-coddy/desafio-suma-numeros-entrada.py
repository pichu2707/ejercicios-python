numbers = input().split(",")


def suma_nambers(numbers):
    total = 0
    for i in numbers:
        if int(i) % 2 == 0:
            total = int(i) + int(i)

        print(total)


suma_nambers(numbers)
