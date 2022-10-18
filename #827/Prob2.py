def main():
    length = int(input())

    for _ in range(length):
        n = int(input())

        nums = list(map(int, input().split(" ")))
        nums.sort()

        flag = True
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                print("NO")
                flag = False
                break
        if flag:
            print("YES")

main()