factor = {
    0 : 0,
    1 : 10,
    2 : 5,
    3 : 10,
    4 : 5,
    5 : 2,
    6 : 5,
    7 : 10,
    8 : 5,
    9 : 10
}
def main():
    n = int(input())

    for _ in range(n):
        a, b = list(map(int, input().split(" ")))
        b = str(b)

        f = factor[a % 10]

        res, zeros = 0, 0
        cur, power = 0, 1
        for char in b:
            c = ord(char) - ord("0")
            cur = 10 * cur + c

            z = calculateZeros((cur - c) * a)
            if z != 0:
                if z == zeros:
                    res = max(res, (cur - c) * a)
                elif z > zeros:
                    zeros = z
                    res = (cur - c) * a

            val = cur - c + f if cur - c + f <= cur else cur - c - 1 + f
            z = calculateZeros(val * a)
            if z != 0:
                if z == zeros:
                    res = max(res, val * a)
                elif z > zeros:
                    zeros = z
                    res = val * a

        if zeros == 0:
            print(a * int(b))
        else:
            print(res)

def calculateZeros(num):
    if num == 0:
        return -1
    res = 0
    while num % 10 == 0:
        res += 1
        num //= 10

    return res

main()



