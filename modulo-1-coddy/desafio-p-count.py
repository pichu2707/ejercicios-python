text = input()


def p_Count(text):
    p_letter = 0
    for chart in text:
        if chart == "p" or chart == "P":
            p_letter += 1
    print(p_letter)


p_Count(text)
