import heapq

def main():
    length = int(input())
    for _ in range(length):
        n = int(input())
        cost = list(map(int, input().split(" ")))
        have = list(map(int, input().split(" ")))

        spent, gain = [], []
        zero = 0

        for i in range(n):
            val = have[i] - cost[i]
            if val == 0:
                zero += 1
            elif val > 0:
                gain.append(val)
            else:
                spent.append(val)

        spent.sort(reverse=True)
        gain.sort()
        res = solver(spent, gain, zero)
        print(res)


def solver(cost, gain, zero):
    i, j = 0, 0
    res = zero // 2
    used = 0
    while i < len(cost) and j < len(gain):
        if gain[j] + cost[i] < 0:
            j += 1
        else:
            res += 1
            i += 1
            j += 1
            used += 1
    left = len(gain) - used
    if zero % 2 == 1:
        left += 1
    res += left // 2

    return res


main()

