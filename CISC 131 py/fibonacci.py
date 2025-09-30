first = 0
second = 1
for x in range(10):
    third = first + second
    first = second
    second = third
    print(third)
    