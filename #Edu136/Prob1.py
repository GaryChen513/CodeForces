length = int(input())

for _ in range(length):
    row, col = list(map(int, input().split(" ")))
    r = min(row, 2)
    c = min(col, 2)

    print(str(r) + " " + str(c))