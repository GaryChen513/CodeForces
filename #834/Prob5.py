def main():
    n = int(input())

    options = [[2,2,3], [2,3,2], [3,2,2]]

    for _ in range(n):
        _, a = list(map(int, input().split(" ")))
        nums = list(map(int, input().split(" ")))

        res = 0
        for opt in options:
            res = max(res, solver(nums, opt, a))

        print(res)

def solver(lst, opt, cur):
    lst.sort()
    j = 0
    for i in range(len(lst)):
        number = lst[i]
        while number >= cur:
            if j == 3:
                return i
            cur *= opt[j]
            j += 1
        cur += lst[i] // 2

    return len(lst)

main()
