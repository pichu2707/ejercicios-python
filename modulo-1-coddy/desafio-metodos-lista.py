lst1 = [1, 2, 3]
lst2 = [4, 5, 6]


def merge(lst1, lst2):
    for i in lst1:
        lst2.append(i)
        lst2.sort()
    print(lst2)


merge(lst1, lst2)
