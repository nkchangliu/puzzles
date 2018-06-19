import statistics

def shortest_move(lst):
    median = int(statistics.median(lst))
    res = 0
    for num in lst:
        res += abs(num - median)
    return res

print(shortest_move([1, 2, 3, 4, 5]))
