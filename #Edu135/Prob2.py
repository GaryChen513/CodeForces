length = int(input())

for _ in range(length):
    n = int(input())
    if n % 2 == 1:
        res1 = [i for i in range(n - 4, n + 1)]
        res2 = [i for i in range(n - 5, 0, -1)]
        res = res2 + res1
    else:
        res = [i for i in range(n - 2, 0, -1)]
        res.append(n - 1)
        res.append(n)
    print(*res)