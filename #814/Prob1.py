def main():
    length = int(input())

    for _ in range(length):
        row, col = list(map(int, input().split(" ")))
        if row % 2 == col % 2:
            print("Tonya")
        else:
            print("Burenka")

main()
