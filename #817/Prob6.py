from collections import Counter
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def main():

    length = int(input())
    for _ in range(length):
        row, col = list(map(int, input().split(" ")))
        graph = []
        for _ in range(row):
            graph.append(list(input()))

        res = solver(graph, row, col)
        print("YES" if res else "NO")

def solver(graph, row, col):

    cnt = 0
    for r in range(row - 1):
        for c in range(col - 1):
            list = [graph[r][c], graph[r + 1][c], graph[r][c + 1], graph[r + 1][c + 1]]
            grids = [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]
            counter = Counter(list)
            if counter["*"] == 3:
                cnt += 1
                if not check(grids, graph):
                    return False

    return sum(s.count('*') for s in graph) == cnt * 3



def check(list, graph):
    for x, y in list:
        if graph[x][y] != "*":
            continue
        for del_x, del_y in DIRECTIONS:
            _x, _y = x + del_x, y + del_y
            if _x < 0 or _x >= len(graph) or _y < 0 or _y >= len(graph[0]):
                continue
            if (_x, _y) in list:
                continue
            if graph[_x][_y] == "*":
                return False

    return True

main()