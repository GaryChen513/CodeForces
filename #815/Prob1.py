length = int(input())

for _ in range(length):
    a,b,c,d = list(map(int, input().split(" ")))

    if a * d == b * c:
        print(0)
    else:
        if a == 0 or c == 0:
            print(1)
        elif not (a * d ) % (b * c) or not (b * c) % (a * d):
            print(1)
        else:
            print(2)