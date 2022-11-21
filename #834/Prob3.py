n = int(input())

for _ in range(n):
    l, r, x = list(map(int, input().split(" ")))
    a, b = list(map(int, input().split(" ")))

    if a == b:
        print("0")
    elif abs(a - b) >= x:
        print("1")
    elif (a + x > r and l + x > a) or (b + x > r and l + x > b):
        print("-1")
    else:
        if a < b:
            if b + x <= r or l + x <= a:
                print("2")
            else:
                print("3")
        else:
            if l + x <= b or a + x <= r:
                print("2")
            else:
                print("3")

