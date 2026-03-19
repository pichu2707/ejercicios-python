lst = input().split(",")

total = 0


def middle(lst):
    n = len(lst)
    mid = n // 2

    if n <= 2:
        print(lst)
    elif n % 2 == 1:
        print(lst[mid - 1 : mid + 2])
    else:
        print(lst[mid - 1 : mid + 1])


middle(lst)
