length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    lst.sort()
    res = float("inf")
    for i in range(len(lst) - 2):
        a,b,c = lst[i], lst[i + 1], lst[i + 2]
        res = min(res, c - a)

    print(res)