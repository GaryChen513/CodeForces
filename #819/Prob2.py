def main():
    length = int(input())

    for _ in range(length):
        n, m = list(map(int, input().split(" ")))
        if n > m:
            print("NO")
        elif n % 2 == 0 and m % 2 == 1:
            print("NO")
        else:
            # lst = solver(m, n)
            print("YES")
            for _ in range(n - 2):
                print(1, end = " ")
            if n % 2 == 1:
                print(1, end = " ")
                print(m - n + 1)
            else:
                print((m - n + 2) // 2 , end = " ")
                print((m - n + 2) // 2)


# def solver(sum_val, n):
#     res = [1 for _ in range(n)]
#     if n % 2 == 1:
#         res[-1] = sum_val - n + 1
#     else:
#         sum_val -= (n - 2)
#         res[-1] = sum_val // 2
#         res[-2] = sum_val // 2
#
#     return res

main()