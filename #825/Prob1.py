from collections import Counter

length = int(input())

for _ in range(length):
    n = int(input())
    lst1 = list(map(int, input().split(" ")))
    lst2 = list(map(int, input().split(" ")))

    count1 = Counter(lst1)
    count2 = Counter(lst2)

    res = 0
    res += abs(count1[1] - count2[1])
    change = res
    for i in range(n):
        if lst1[i] == lst2[i]:
            continue
        if change:
            change -= 1
            continue
        res += 1
        break

    print(res)
