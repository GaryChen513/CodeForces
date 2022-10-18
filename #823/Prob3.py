def main():
    length = int(input())
    for _ in range(length):
        string = input()

        res = solver(string)
        print(res)

def solver(string):
    heap = []
    stack = []

    for letter in string:
        letter = int(letter)
        while stack and stack[-1] > letter:
            num = min(stack.pop() + 1, 9)
            heap.append(num)
        stack.append(letter)
    stack = stack + heap
    stack.sort()
    stack = [str(s) for s in stack]
    return "".join(stack)

main()