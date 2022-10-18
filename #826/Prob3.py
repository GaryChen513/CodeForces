def main():
    length = int(input())

    for _ in range(length):
        n = int(input())

        lst = list(map(int, input().split(" ")))

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + lst[i]

        index_mapping = dict()
        for i in range(n + 1):
            index_mapping[prefix_sum[i]] = i

        res = n
        for seg in range(1, n + 1):
            if prefix_sum[-1] % seg == 0:
                res = min(solver(index_mapping, prefix_sum[-1] // seg, prefix_sum[-1]), res)
        print(res)

def solver(mapping, seg_val, total):
    res = 1
    cur_sum = 0
    while cur_sum < total:
        nex_val = cur_sum + seg_val
        if nex_val not in mapping:
            return len(mapping)
        res = max(res, mapping[nex_val] - mapping[cur_sum])
        cur_sum = nex_val

    return res

main()