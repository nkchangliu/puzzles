def number_longest_increasing(lst):
    if not lst:
        return 0
    res = [(1, 1)] * len(lst)
    for i in range(1, len(lst)):
        length, count = 1, 1
        for j in range(0, i):
            if lst[j] < lst[i] and res[j][0] + 1 > length:
                length, count = res[j][0] + 1, res[j][1]
            elif lst[j] < lst[i] and res[j][0] + 1 == length:
                count += res[j][1]
        res[i] = (length, count)
    return count_ways(res)

def count_ways(res):
    max_length, max_ways = 0, 0
    for length, ways in res:
        if length > max_length:
            max_length, max_ways = length, ways
        elif length == max_length:
            max_ways += ways
    return max_ways

print(number_longest_increasing([2, 2, 2, 2, 2]))

