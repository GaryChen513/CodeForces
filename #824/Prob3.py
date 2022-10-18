def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        line = input()

        res = solver(line)

        print(res)

def solver(string):
    parents = [chr(i) for i in range(ord("a"), ord("a") + 26)]
    seen = set()

    res = [""] * len(string)
    i = 0
    for letter in string:
        p = assignParent(seen, parents, letter)
        parents[ord(letter) - ord("a")] = p
        seen.add(p)
        res[i] = p
        i += 1
    # print(res)
    return "".join(res)

def assignParent(seen, parents, letter):
    if parents[ord(letter) - ord("a")] != letter:
        return parents[ord(letter) - ord("a")]

    for i in range(26):
        char = chr(i + ord("a"))
        if char in seen:
            continue
        p1 = find(char, parents)
        p2 = find(letter, parents)
        if p1 == p2:
            continue

        return char

    for i in range(26):
        char = chr(i + ord("a"))
        if char in seen:
            continue
        return char

def find(c,parents):
    while parents[ord(c) - ord("a")] != c:
        c = parents[ord(c) - ord("a")]

    return c

main()