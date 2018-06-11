def predict_winner(lst):
    cache = [[0 for i in range(len(lst))] for j in range(len(lst))]
    for i in range(len(lst)):
        cache[i][i] = lst[i]

    for s in range(len(lst) - 2, -1, -1):
        for e in range(s + 1, len(lst), 1):
            cache[s][e] = max(lst[s] - cache[s + 1][e], lst[e] - cache[s][e - 1])
    return cache[0][len(lst) - 1] >= 0

print(predict_winner([1, 5, 2]))
