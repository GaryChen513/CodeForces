def main():
    length = int(input())
    for _ in range(length):
        n, k, r, c = list(map(int, input().split(" ")))
        res = [["."] * n for _ in range(n)]

        solver((r - 1) % k, (c - 1) % k, res, k, n)

        for line in res:
            print("".join(line))

def solver(r, c, grid, k, n):
    _r, _c = 0, 0
    arr_r, arr_c = [r], [c]
    for _ in range(k - 1):
        if _r == r:
            _r += 1
        if _c == c:
            _c += 1
        arr_r.append(_r)
        arr_c.append(_c)
        _r += 1
        _c += 1
    t = n // k
    for i in range(t ** 2):
        t_r = i // t
        t_c = i % t
        for j in range(len(arr_r)):
            _r = t_r * k + arr_r[j]
            _c = t_c * k + arr_c[j]
            grid[_r][_c] = "X"

main()