def main():
    length = int(input())
    for _ in range(length):
        n = int(input())
        lst1 = list(map(int, input().split(" ")))
        lst2 = list(map(int, input().split(" ")))


        max_val = max(lst1)
        min_val = min(lst2)

        for i in range(len(lst1)):
            lst1[i] = min(max_val, lst2[i])
            lst1[i] = max(min_val, lst1[i])
        # print(lst1, lst2)
        print("Yes" if solver(0, lst1, lst2, lst1[0]) else "No")

def solver(index, lst1, lst2, min_val):
    if index == len(lst1):
        return True

    n = len(lst1)
    if lst1[index] == lst2[index]:
        return solver(index + 1, lst1, lst2, lst2[index])

    if lst1[index % n] <= lst1[(index + 1) % n]:

        if abs(min_val - lst2[index]) <= 1:
            # print(lst1, lst2, index, 0)
            lst1[index] = lst2[index]
            min_val = min(min_val, lst2[index]) if min_val > lst2[index] else lst2[index]
            return solver(index + 1, lst1, lst2, min_val)
        else:
            # print(lst1, lst2, index, 1)
            return False
    else:
        # print(lst1, lst2, index, 2)
        return False

main()