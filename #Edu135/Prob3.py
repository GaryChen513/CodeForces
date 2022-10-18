import heapq

def main():
    length = int(input())

    for _ in range(length):
        n = int(input())
        lst1 = list(map(int, input().split(" ")))
        heap1 = [-num for num in lst1]
        lst2 = list(map(int, input().split(" ")))
        heap2 = [-num for num in lst2]

        heapq.heapify(heap1)
        heapq.heapify(heap2)

        res = solver(heap1, heap2)
        print(res)


def solver(heap1, heap2):
    res = 0
    while heap1 and heap2:

        if heap1[0] == heap2[0]:
            heapq.heappop(heap1)
            heapq.heappop(heap2)
            continue
        if -heap1[0] > -heap2[0]:
            top = heapq.heappop(heap1)
            heapq.heappush(heap1, getDigit(top))
        else:
            top = heapq.heappop(heap2)
            heapq.heappush(heap2, getDigit(top))
        res += 1

    return res


def getDigit(number):
    number = -number
    res = 0
    while number > 0:
        res += 1
        number //= 10
    return -res

main()
