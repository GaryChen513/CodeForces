length = int(input())

for _ in range(length):
    n, k = list(map(int, input().split(" ")))

    count = 0
    no_k = []
    need_k = []
    rest = []
    for i in range(1, n + 1):
        if i % 4 == 0:
            no_k.append(i)
        elif (i + k) % 4 == 0:
            need_k.append(i)
        else:
            rest.append(i)
    if len(no_k) + len(need_k) < len(rest):
        print("NO")
    else:
        print("YES")
        l = min(len(no_k), len(rest))
        for i in range(l):
            print(str(rest[i]) + " " + str(no_k[i]))

        j = 0
        if l == len(no_k):
            for i in range(l, len(rest)):
                print(str(need_k[j]) + " " + str(rest[i]))
                j += 1
        else:
            for i in range(l, len(no_k)):
                print(str(need_k[j]) + " " + str(no_k[i]))
                j += 1

        m = len(need_k) - 1
        while j < m:
            print(str(need_k[m]) + " " + str(need_k[j]))
            j += 1
            m -= 1
    print(no_k)
    print(need_k)
    print(rest)

