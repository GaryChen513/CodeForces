from collections import Counter
length = int(input())

for _ in range(length):
    n,c = list(map(int, input().split(" ")))
    nums = list(map(int, input().split(" ")))

    counter = Counter(nums)
    res = 0
    for key, val in counter.items():
        if val >= c:
            res += c
        else:
            res += val

    print(res)
