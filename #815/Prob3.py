DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def main():
    length = int(input())

    for _ in range(length):
        row, col = list(map(int, input().split(" ")))

        graph = []
        for _ in range(row):
            line = input()
            graph.append(line)

        res = solver(graph, row, col)
        sum_val = 0
        for r in range(row):
            for c in range(col):
                if graph[r][c] == "1":
                    sum_val += 1

        print(sum_val - 2 + res)


def solver(graph, row, col):
    res = 0
    for r in range(row):
        for c in range(col):
            if graph[r][c] == "0":
                res = 1
                for _r, _c in DIRECTIONS:
                    if not isValid(r + _r, c + _c, row, col):
                        continue
                    if graph[r + _r][c + _c] == "0":
                        return 2
    return res


def isValid(r, c, row, col):
    if r < 0 or r >= row or c < 0 or c >= col:
        return False
    return True


main()
