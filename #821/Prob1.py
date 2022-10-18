length = int(input())

for _ in range(length):
    n, k = list(map(int, input().split(" ")))
    lst = list(map(int, input().split(" ")))

    res = [-1] * k
    for i in range(n):
        if lst[i] > res[i % k]:
            res[i % k] = lst[i]

    print(sum(res))