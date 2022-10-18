def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        lst = list(map(int, input().split(" ")))

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            cur = lst[i]
            if cur <= i and dp[i - cur]:
                dp[i + 1] = True
            if cur + i < n and dp[i]:
                dp[i + 1 + cur] = True
        if dp[-1]:
            print("YES")
        else:
            print("NO")

main()