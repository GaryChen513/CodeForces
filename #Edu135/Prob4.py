def main():
    for i in range(2):
        for j in range(3):
            if j == 1:
                break
        print(i)


def solver(str):
    n = len(str)
    canDraw = False
    if n % 2 == 1:
        for start in range(n):
            first, second = startGame(start, start, str)
            if first > second:
                if n % 2 == 1:
                    print("Alice")
                    return
            if first == second:
                canDraw = True
        if canDraw:
            print("Draw")
        else:
            print("Bob")

    else:
        for start in range(n):
            first, second = startGame(start, start, str)
            if first > second:
                if n % 2 == 1:
                    print("Bob")
                    return
            if first == second:
                canDraw = True
        if canDraw:
            print("Draw")
        else:
            print("Alice")

#
# def startGame(start, end,  str):
#     res = [[], []]
#     round = 0


main()



