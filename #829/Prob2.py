def main():
    length = int(input())

    for _ in range(length):
        n = int(input())

        print(1, end=" ")
        for i in range(n, 1, -1):
            print(i, end=" ")
        print()
main()