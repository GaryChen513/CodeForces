def main():
    length = int(input())
    for _ in range(length):
        n, pos = list(map(int, input().split(" ")))
        lst = list(map(int, input().split(" ")))

        res = solver(lst, pos - 1)

        if res:
            print("YES")
        else:
            print("NO")


def solver(lst, pos):
    if lst[pos] < 0:
        return False
    if pos == 0 or pos == len(lst) - 1:
        return True

    length = 1
    new_lst = []
    new_pos = -1

    sum_val = lst[0]
    isNegtive = True if lst[0] < 0 else False
    for i in range(1, len(lst)):
        if (isNegtive and lst[i] >= 0) or (not isNegtive and lst[i] < 0):
            length += 1
            new_lst.append(sum_val)
            sum_val = lst[i]
            isNegtive = False if isNegtive else True;
        else:
            sum_val += lst[i]

        if i == pos:
            new_pos = length - 1

    new_lst.append(sum_val)

    life = new_lst[new_pos]
    if life < 0:
        return False
    left,right = new_pos - 1, new_pos + 1
    while left >= 0 and right < len(new_lst):

        if new_lst[left] >= 0:
            life += new_lst[left]
            left -= 1
        if new_lst[right] >= 0:
            life += new_lst[right]
            right += 1
        if left < 0 or right >= len(new_lst):
            return True

        if new_lst[left] < new_lst[right]:
            life += new_lst[right]
            right += 1
        else:
            life += new_lst[left]
            left -= 1

        if life < 0:
            return False

    return True




main()

