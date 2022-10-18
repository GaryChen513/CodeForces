length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    min_val = min(lst)
    max_val = 2 * min_val

    res = 0
    for num in lst:
        if num < max_val:
            continue
        res += (num // (max_val - 1) - 1)

        if num % (max_val - 1):
            res += 1

    print(res)