def main():
    n = int(input())

    for _ in range(n):
        solver()

def solver():
    m, s = list(map(int, input().split(" ")))
    nums = list(map(int, input().split(" ")))

    nums.sort()
    mv = max(nums)
    j = 0
    for i in range(1, mv + 1):
        if i == nums[j]:
            j += 1
            continue
        s -= i
        if s < 0:
            print("NO")
            return

    while s > 0:
        mv += 1
        s -= mv
    if s == 0:
        print("YES")
    else:
        print("NO")


main()


