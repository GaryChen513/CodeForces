def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        lst = list(map(int, input().split(" ")))

        cnt = 0
        for num in lst:
            cnt += solver(num)

        if cnt >= n:
            print(0)
            continue

        res = 0
        twos = [solver(i) for i in range(1, n + 1)]
        twos.sort(reverse=True)
        for i in range(n):
            cnt += twos[i]
            res += 1
            if cnt >= n:
                break

        if cnt < n:
            print(-1)
        else:
            print(res)

def solver(num):
    cnt = 0
    while (num >> cnt) & 1 == 0:
        cnt += 1
    return cnt


main()

