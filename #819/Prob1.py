length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    res = 0
    for i in range(n - 1):
        res = max(res, lst[i] - lst[i + 1])
    res = max(res, max(lst) - lst[0])
    res = max(res, lst[-1] - min(lst))

    print(res)