def main():

    length = int(input())
    mod = 998244353

    for _ in range(length):
        n = int(input())

        alex, boris = 1, 0
        for i in range(2, n // 2 + 1):
            total = combo(i * 2, i)
            new_boris = alex + combo(i * 2 - 2, i - 2)
            new_alex = total - 1 - new_boris
            alex, boris = new_alex, new_boris

        print(str((alex + mod) % mod) + " " + str((boris + mod) % mod) + " " + "1")


def combo(first, second):
    if second == 0:
        return 1
    top, bot = 1, 1
    for i in range(1, second + 1):
        top *= first - second + i
        bot *= i
    return top // bot


main()