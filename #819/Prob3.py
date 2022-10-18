length = int(input())

for _ in range(length):
    n = int(input())
    line = input()
    minus = 0

    stack = []
    parent = [-1] * (2 * n)
    for i in range(2 * n):
        letter = line[i]
        if letter == "(":
            stack.append(i)
            if i - 1 >= 0 and line[i - 1] == ")":
                parent[i] = parent[i - 1]
        else:
            index = stack.pop()
            parent[i] = index
    # print(parent)
    res = 0
    for val in parent:
        if val == -1:
            res += 1

    print(res)