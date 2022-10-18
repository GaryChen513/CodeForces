from collections import defaultdict

def main():

    length = int(input())

    for _ in range(length):
        n = int(input())
        lst = list(map(int, input.split(" ")))

        res = solver(lst)
        print(res)


def solver(lst):
    mapping = defaultdict(set)
    for i in range(lst):
        mapping[lst[i]].add(i)

    n = len(lst)
    right_most = -1
    prev = float("inf")
    res = 0
    for i in range(n - 1, -1, -1):
        if lst[i] <= prev:
            prev = lst[i]
        else:
            lst[i] = 0
            right_most = max(mapping[lst[i]][-1], right_most)
            for index in
            prev = 0


