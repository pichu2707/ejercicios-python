num = int(input())


def sigma(n):
    result = 0
    for i in range(n + 1):
        result += i
    print(result)


sigma(num)
