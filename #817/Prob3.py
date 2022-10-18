from collections import Counter

length = int(input())

mapping = {
    1 : 3,
    2 : 1,
    3 : 0

}

for _ in range(length):
    n = int(input())
    line1 = input().split(" ")
    line2 = input().split(" ")
    line3 = input().split(" ")
    lines = [line1, line2, line3]

    counter = Counter(line1 + line2 + line3)

    for line in lines:
        res = 0
        for word in line:
            res += mapping[counter[word]]
        print(res, end=" ")
    print()