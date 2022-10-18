length = int(input())

for _ in range(length):
    num = int(input())

    left = num - 4
    base = left // 3
    if left % 3 == 0 or left % 3 == 1:
        print(max(base - 1, 0))
    elif left % 3 == 2:
        print(base)
