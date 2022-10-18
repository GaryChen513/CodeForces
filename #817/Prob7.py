length = int(input())

for _ in range(length):
    n = int(input())

    res = 0
    for i in range(n - 1):
        print(i, end=" ")
        res ^= i

    num1 = 1 << 30
    if n >= 1:
        print(num1, end=" ")
    num2 = 1 << 29
    if n >= 2:
        print(num2, end=" ")
    res ^= num1
    res ^= num2
    if n >= 3:
        print(res, end=" ")
    print()