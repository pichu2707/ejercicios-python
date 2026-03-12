lst = [1, 5, 3, 8, 2, 7, 4, 6]
threshold = 4


def combine_and_filter(lst, threshold):
    list_filter = []
    for i in lst:
        if i > threshold:
            list_filter.append(i)
    list_filter.sort()
    print(list_filter)


combine_and_filter(lst, threshold)
