length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    prev = lst[0]
    res = 0
    ways = []

    for i in range(n - 1):
        if i - 1 >= 0:
            prev = lst[i - 1]
        if lst[i] > lst[i + 1]:
            if (prev + lst[i]) & 1 == 1:
                ways.append((i, i + 1))
                res += 1
                lst[i] = prev
            elif (lst[i] + lst[i + 1]) & 1 == 0:
                ways.append((i + 1, i + 2))
                res += 1
                lst[i] = lst[i + 1]
            else:
                ways.append((i, i + 2))
                ways.append((i + 1, i + 2))
                res += 2
                lst[i] = prev
                lst[i + 1] = prev
        print(i, lst)
    print(res)
    if res:
        for a,b in ways:
            print(str(a) + " " + str(b))