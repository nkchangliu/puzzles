
def max_length_pairs(pairs):
    pairs = sorted(pairs, key = lambda pair:(pair[0], pair[1]))
    res = [1] * len(pairs)

    for i in range(1, len(pairs)):
        max_num = res[0]
        for j in range(i):
            if pairs[i][0] > pairs[j][1] and res[j] + 1 > max_num:
                max_num = res[j] + 1
        res[i] = max_num

    return res[-1]

print(max_length_pairs([[3,4],[2,3],[1,2]]))
