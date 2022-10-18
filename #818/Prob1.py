length = int(input())

for _ in range(length):
    number = int(input())
    res = 0
    if number // 3 > 0:
        res += (4 * (number // 3))
    if number // 2 > 0:
        res += ((number // 2 - number // 3) * 2)

    res += number
    print(res)