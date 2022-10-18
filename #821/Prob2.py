length = int(input())

for _ in range(length):
    n,x,y = list(map(int, input().split(" ")))

    if x != 0 and y != 0:
        print(-1)
    elif x + y == 0:
        print(-1)
    elif (n - 1) % (x + y) != 0:
        print(-1)
    else:
        i = 2
        while i <= n:
            for _ in range(x+y):
                print(i, end=" ")
            i += (x + y)
        print()