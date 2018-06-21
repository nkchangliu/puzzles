def solve(n, k):
    combins = []
    combination(combins, [], 1, n, k)
    return combins

def combination(combins, combin, start, n, k):
    if k == 0:
        print(combin)
        print(combins)
        combins.append(combin[:])
        return
    for i in range(start, n+1):
        combin.append(i)
        combination(combins, combin, i + 1, n, k -1)
        combin.pop()

def combinations(n, k):
    results = solve_helper(1, n, k)
    return results

def solve_helper(start, n, k):
    if k == 0:
        return [[]]
    elif start > n:
        return
    sub_results = solve_helper(start + 1, n, k - 1)
    sub_results2 = solve_helper(start + 1, n, k)
    results = []
    if sub_results is not None:
        for sub in sub_results:
            sub.append(start)
            results.append(sub)
    if sub_results2 is not None:
        results += sub_results2
    return results



print(combinations(4, 2))
