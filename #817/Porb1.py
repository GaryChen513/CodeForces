from collections import Counter

def main():
    length = int(input())
    counter = Counter("Timur")
    for _ in range(length):
        n = input()
        name = input()
        counter1 = Counter(name)
        print(solver(counter, counter1))


def solver(counter, counter1):
    if len(counter) != len(counter1):
        return "No"
    for key, val in counter.items():
        if key not in counter1:
            return "No"
        if counter[key] != counter1[key]:
            return "No"

    return "Yes"

main()