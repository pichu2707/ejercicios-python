lst = [5, 3, 7, 1, 6, 2, 54, 123, -98, 32]


def prod(lst):
    result = 1
    for i in lst:
        result *= i
    print(result)


prod(lst)
