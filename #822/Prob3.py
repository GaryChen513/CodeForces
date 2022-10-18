def main():
    length = int(input())

    for _ in range(length):
        n = int(input())

        str = input()
        calculated = [-1] * n

        res = 0
        for i in range(1, n + 1):
            j = i - 1
            if str[j] == "1":
                continue
            res += solver(i, str, calculated)

        print(res)


def solver(num, str, calculated):
    res = 0
    i = 1
    while num * i - 1 < len(str) and str[num * i - 1] == "0":
        if calculated[num * i - 1] == -1:
            res += num
            calculated[num * i - 1] = 1
        i += 1


    return res

main()


