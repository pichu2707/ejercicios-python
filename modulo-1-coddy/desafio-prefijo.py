numbers = input()
prefix = input()


def aggregate(numbers, prefix):
    new_list = numbers.split()
    new_text = f" {prefix}".join(new_list)
    print(prefix + new_text)


aggregate(numbers, prefix)
