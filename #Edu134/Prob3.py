import bisect
def main():

    length = int(input())

    for _ in range(length):
        n = int(input())
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))

        mins = []
        for number in a:
            index = bisect.bisect_left(b, number)
            mins.append(b[index] - number)
        print(*mins)

        maxs = [-1] * len(a)
        pos = len(a) - 1
        for i in range(len(a) - 1, -1, -1):
            index = bisect.bisect_left(b, a[i])
            maxs[i] = max(b[index], b[pos]) - a[i]
            if pos <= index:
                pos = index - 1
        print(*maxs)


# def solver(arr, next_arr, i):
#     res = i - 1
#     j = 0
#
#     while j < len(next_arr) and i < len(arr):
#         if arr[i] <= next_arr[j]:
#             i += 1
#             j += 1
#         else:
#             res = max(res, j)
#             j += 1
#
#     if j < len(next_arr):
#         return len(next_arr) - 1
#     return res

main()