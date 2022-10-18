length = int(input())

for _ in range(length):
    n, k = list(map(int, input().split(" ")))

    lst = list(map(int, input().split(" ")))

    res = 0
    for i in range(k):
        if lst[i] > k:
            res += 1

    print(res)