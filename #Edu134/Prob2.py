length = int(input())

for _ in range(length):
    row, col, x, y, d = list(map(int, input().split(" ")))

    if (x + d >= row and y + d >= col) or (x - d <= 1 and y - d <= 1):
        print(-1)
    elif x + d >= row and x - d <= 1:
        print(-1)
    elif y + d >= col and y - d <= 1:
        print(-1)
    else:
        print(row + col - 2)