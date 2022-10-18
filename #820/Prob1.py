length = int(input())

for _ in range(length):
    a,b,c = list(map(int, input().split(" ")))
    first = a - 1
    second = abs(b - c) + c - 1

    if first < second:
        print(1)
    elif first > second:
        print(2)
    else:
        print(3)