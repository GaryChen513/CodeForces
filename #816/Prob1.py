length = int(input())

for _ in range(length):
    row, col = list(map(int, input().split(" ")))

    res = (row - 1) + (col - 1) + min(row - 1, col - 1)
    if row == 1 and col == 1:
        print(res)
    else:
        print(res + 1)