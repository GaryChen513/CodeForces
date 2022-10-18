from collections import Counter
length = int(input())

for _ in range(length):
    graph = ""
    graph += input()
    graph += input()

    counter = Counter(graph)
    print(len(counter) - 1)