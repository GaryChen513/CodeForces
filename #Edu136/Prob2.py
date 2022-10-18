length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    isOnly = True
    res = [lst[0]]
    for i in range(1, n):
        if lst[i] == 0:
            res.append(res[-1])
            continue
        if res[-1] > lst[i]:
            isOnly = False
            break
        res.append(lst[i] + res[-1])

    if not isOnly:
        print(-1)
    else:
        print(*res)