list = [-1, -2, -3, -4]


def sum_elements(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    print(result)


sum_elements(list)
