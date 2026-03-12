list1 = [True, False, True]
index = 2
list2 = [False]


def change_element(list1, index, list2):
    element = list2[0]
    list1[index] = element
    print(list1)


change_element(list1, index, list2)
