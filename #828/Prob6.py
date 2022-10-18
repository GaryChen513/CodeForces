import math

length = int(input())

for _ in range(length):
    a,b,c,d = list(map(int, input().split(" ")))

    factor1 = math.gcd(a,b)
    factor2 = a//factor1 + b//factor1

    factor = max(factor1, factor2)
    cnt = min(factor1, factor2)

    flag = True
    for k in range(1, cnt):
        m = cnt - k
        if m > k:
            continue
        if a // (factor*m) < c // (factor*m) and b//(factor*k) < d//(factor*k):
            print(factor*m*(a // (factor*m) + 1), end=" ")
            print(factor*k*(a // (factor*m) + 1))
            flag = False
            break
    if flag:
        print("-1 -1")

