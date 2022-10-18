from math import sqrt

def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        nums = list(map(int, input().split(" ")))
        res = solver(nums, n)
        print(res)


def solver(nums, n):
    for i in range(n - 1, -1, -1):
        if isPrime(nums[i]):
            j = n - 1
            if nums[i] == 1:
                return (i + 1) * 2
            while j > 0:
                if nums[i] == 2:
                    if nums[j] % nums[i] == 0:
                        j -= 1
                        continue
                if nums[i] == nums[j]:
                    j -= 1
                    continue
                break
            if j >= 0:
                return i + j + 2
    return -1


def isPrime(num):
    if num == 1:
        return True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
main()