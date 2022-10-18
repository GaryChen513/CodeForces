def main():
    length = int(input())

    for _ in range(length):
        input()
        grid = []
        for _ in range(8):
            line = input()
            grid.append(line)

        Rlast = False
        for i in range(8):
            cntR, cntC = 0, 0
            for j in range(8):
                if grid[i][j] == "R":
                    cntR += 1
                if grid[j][i] == "R":
                    cntC += 1
            if cntC == 8 or cntR == 8:
                Rlast = True
                break
        if Rlast:
            print("R")
        else:
            print("B")


main()
