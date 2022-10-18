length = int(input())

for _ in range(length):
    n = int(input())
    line = input()
    res = 0
    diff = []
    for i in range(n):
        if line[i] == "L":
            res += i
            diff.append(max(0, (n - i - 1) - i))
        else:
            res += (n - 1 - i)
            diff.append(max(0, i - (n - i - 1)))

    diff.sort(reverse=True)
    for i in range(n):
        res += diff[i]
        print(res, end=" ")
    print()