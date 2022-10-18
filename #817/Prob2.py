length = int(input())

for _ in range(length):
    n = int(input())
    str1 = input()
    str2 = input()

    new_str1 = str1.replace("G", "B")
    new_str2 = str2.replace("G", "B")
    if new_str1 == new_str2:
        print("Yes")
    else:
        print("No")
