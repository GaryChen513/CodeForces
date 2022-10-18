length = int(input())

for _ in range(length):
    n, color = input().split(" ")
    line = input()
    if color == "g":
        print(0)
        continue
    f_g = -1
    r, g= -1, -1
    res = -1
    for i in range(int(n)):
        char = line[i]
        if char == "g":
            f_g = i if f_g == -1 else f_g
            g = i
            if r != -1:
                res = max(g - r, res)
                r = -1
        if char == color and r == -1:
            r = i
    if r != -1:
        res = max(res, int(n) - r + f_g)
    print(res)
