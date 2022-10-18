length = int(input())

for _ in range(length):
    n = int(input())
    string = input()

    res = []
    i = 0
    while i < n:
        if i + 2 < n and string[i + 2] == "0":
            if i + 3 < n and string[i + 3] == "0":
                order = int(string[i])
                i += 1
            else:
                order = int(string[i: i + 2])
                i += 3
        else:
            order = int(string[i])
            i += 1
        letter = chr(ord("a") + order - 1)
        res.append(letter)

    print("".join(res))
