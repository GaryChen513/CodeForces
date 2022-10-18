from collections import Counter
def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        s_cnt = [0] * 26
        t_cnt = [0] * 26
        for _ in range(n):
            d, k, word = input().split(" ")
            k = int(k)
            counter = Counter(word)

            if d == "1":
                for key, val in counter.items():
                    index = ord(key) - ord("a")
                    s_cnt[index] += val
            else:
                for key, val in counter.items():
                    index = ord(key) - ord("a")
                    t_cnt[index] += val

            res = solver(s_cnt, t_cnt)
            print(res)

def solver(arr1, arr2):
    isLess = False
    for i in range(26):
        if arr1[i] == arr2[i]:
            continue
        if arr1[i] < arr2[i] and not isLess:
            isLess = True
            continue
        if isLess:
            return "NO"
    return "YES"

main()