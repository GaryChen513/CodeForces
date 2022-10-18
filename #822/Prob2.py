length = int(input())

for _ in range(length):
    n = int(input())

    for level in range(1, n + 1):
        for i in range(level):
            if i == 0:
                print("1", end=" ")
            elif i >= 1 and i == level - 1:
                print("1", end= " ")
            else:
                print("0", end=" ")
        print()

