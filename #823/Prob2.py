def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        pos = list(map(int, input().split(" ")))
        dressing = list(map(int, input().split(" ")))

        arr = [(a,b) for a,b in zip(pos, dressing)]
        arr.sort()

        res = solver(arr)
        print(max(res, 0))

def solver(arr):
    left = 0
    distance = float("inf")
    for i in range(len(arr)):
        if distance > arr[i][0] - arr[i][1]:
            left = i
            distance = arr[i][0] - arr[i][1]

    right = len(arr) - 1
    space = -float("inf")
    for i in range(len(arr)):
        if space < arr[i][0] + arr[i][1]:
            right = i
            space = arr[i][0] + arr[i][1]

    if left == right:
        return arr[left][0]
    return (arr[left][0] - arr[left][1] + arr[right][0] + arr[right][1]) / 2


main()