length = int(input())

for _ in range(length):
    n = int(input())
    lst = list(map(int, input().split(" ")))

    print(lst.index(max(lst)) + 1)