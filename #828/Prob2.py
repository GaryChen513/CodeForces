length = int(input())

for _ in range(length):
    n,q = list(map(int, input().split(" ")))

    lst = list(map(int, input().split(" ")))
    even, odd = 0, 0
    cntE, cntO = 0, 0
    for num in lst:
        if num & 1:
            odd += num
            cntO += 1
        else:
            even += num
            cntE += 1

    for _ in range(q):
        command, val = list(map(int, input().split(" ")))
        if command == 0:
            if val & 1:
                odd += (even + val * cntE)
                even = 0
                cntO += cntE
                cntE = 0
            else:
                even += val * cntE
        else:
            if not (val & 1):
                odd += val * cntO
            else:
                even += (odd + val * cntO)
                odd = 0
                cntE += cntO
                cntO = 0
        print(even + odd)


