length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    lst.sort()
    print(lst[-1] + lst[-2] - lst[0] - lst[1])

