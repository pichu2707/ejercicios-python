lst = input().split(",")
# penguin,elephant,koala,tiger,dolphin,giraffe,kangaroo,zebra,lion,panda


def large_words(lst):
    words = []
    count_letter = 0
    for i in lst:
        if len(i) > 5:
            words.append(i)
    print(words)


large_words(lst)
