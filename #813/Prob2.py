length = int(input())

for _ in range(length):
    n = int(input())
    start = 1
    if n % 2 == 1:
        print(start, end= " ")
        start += 1

    while start <= n:
        print(start + 1, end = " ")
        print(start, end = " ")
        start += 2

    print()
