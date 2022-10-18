length = int(input())

for _ in range(length):
    n = int(input())

    if n == 3:
        print("-1", end=" ")
    else:
        print(n, end=" ")
        print(n - 1, end=" ")
        for i in range(1, n - 1):
            print(i, end=" ")
    print()
