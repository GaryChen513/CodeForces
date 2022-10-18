length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    index = 0
    res = 0
    for i in range(n):
        index += 1
        if lst[i] < index:
            index = lst[i]
        res += index

    print(res)