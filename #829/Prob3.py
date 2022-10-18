import heapq

def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        lids = input()
        lids = lids[::-1]
        m = list(map(int, input().split(" ")))
        m = m[::-1]

        dp = [0 for _ in range(n + 2)]

        cnt = 0
        for i in range(1, n + 1):
            nex = [0] * (n + 2)
            if lids[i - 1] == "1":
                cnt += 1
            if not cnt:
                continue
            for c in range(cnt - 1, -1, -1):
                if lids[i - 1] == "1":
                    nex[c] = max(dp[c], dp[c] + m[i - 1])
                    if c >= 1:
                        nex[c] = max(nex[c], dp[c - 1])
                else:
                    nex[c] = max(dp[c], dp[c + 1] + m[i - 1])
            dp = nex
        print(dp[0])

main()