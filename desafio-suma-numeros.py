numbers = input().split(",")

total = 0
for i in numbers:
    if int(i) % 2 == 0:
        total += int(i)
print(total)
