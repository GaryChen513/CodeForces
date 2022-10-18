length = int(input())

for _ in range(length):
    string = input()

    arr = [None] * len(string)
    for i in range(len(string)):
        letter = string[i]
        order = ord(letter) - ord("a") + 1
        arr[i] = (order, i + 1)

    if ord(string[-1]) >= ord(string[0]):
        arr.sort()
    else:
        arr.sort(key=lambda x: (-x[0], x[1]))

    found_first = False
    cost, prev, number = 0, None, 0
    res = []
    for val, index in arr:
        if index == 1:
            prev = val
            found_first = True

        if not found_first:
            continue
        cost += abs(val - prev)
        if index == len(string):
            res.append(index)
            break
        prev = val
        number += 1
        res.append(index)

    print(str(cost) + " " + str(number + 1))
    print(*res)
