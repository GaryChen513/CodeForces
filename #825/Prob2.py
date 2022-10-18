import math

length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    isNO = False
    for i in range(n - 2):
        if math.gcd(lst[i], lst[i + 2]) != math.gcd(lst[i], math.gcd(lst[i + 1], lst[i + 2])):
            print("NO")
            isNO = True
            break

    if not isNO:
        print("Yes")