from collections import defaultdict
from bisect import bisect_right

length = int(input())

for _ in range(length):
    n, q = list(map(int, input().split(" ")))
    steps = list(map(int, input().split(" ")))
    trials = list(map(int, input().split(" ")))

    height = 0
    mapping = defaultdict(int)

    cur_max = 0
    for i in range(n):
        height += steps[i]
        cur_max = max(cur_max, steps[i])
        mapping[cur_max] = height

    lst = [key for key in mapping.keys()]
    lst.sort()

    for t in trials:
        index = bisect_right(lst, t)
        if index == 0:
            print(0, end=" ")
        else:
            print(mapping[lst[index - 1]], end= " ")

    print()
