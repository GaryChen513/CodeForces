def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        cur = list(map(int, input().split(" ")))

        res = solver(n, cur)
        print(res)

def solver(n, cur):
    res = 0
    while len(cur) > 1:
        nex = []

        for i in range(0,n,2):
            half = n // 2
            first = cur[0] > half
            second = cur[n//2] > half

            if abs(cur[i] - cur[i + 1]) != 1:
                return -1
            if i < half and (cur[i] > half) != first:
                return -1
            if i >= half and (cur[i] > half) != second:
                return -1
            if cur[i] > cur[i + 1]:
                res += 1
            nex.append(max(cur[i], cur[i + 1]) // 2)
        n //= 2
        cur = nex

    return res

main()