n = int(input())

parttern = "Yes"
for _ in range(n):
    line = input()
    i = parttern.find(line[0])
    if i == -1:
        print("NO")
    else:
        isSub = True
        for j in range(1, len(line)):
            i += 1
            if parttern[i % 3] != line[j]:
                isSub = False
                break
        if isSub:
            print("YES")
        else:
            print("NO")
