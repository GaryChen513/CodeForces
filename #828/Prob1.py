def main():
    length = int(input())

    for _ in range(length):
        n = int(input())

        nums = list(map(int, input().split(" ")))
        string = input()
        solver(nums, string, n)

def solver(nums, string, n):
        mapping = dict()

        for i in range(n):
            c = string[i]
            if nums[i] not in mapping:
                mapping[nums[i]] = c
            else:
                if mapping[nums[i]] != c:
                    print("NO")
                    return
        print("YES")
        return

main()