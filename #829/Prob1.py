def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        lst = list(map(int, input().split(" ")))

        a = 10 - n
        comb = a * (a - 1) // 2
        print(comb*6)

main()