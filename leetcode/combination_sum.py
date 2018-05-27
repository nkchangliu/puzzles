import itertools

def combination_sum(candidates, target):
    cache = {}
    solution = com_sum(candidates, target, cache)
    solution.sort()
    return list(k for k, _ in itertools.groupby(solution))

def com_sum(candidates, target, cache):
    if target == 0:
        return [[]]
    if target < 0:
        return []
    if target in cache:
        return cache[target]

    solution = []
    for num in candidates:
        sub_sols = com_sum(candidates, target - num, cache)
        sub_sols = add_num(sub_sols, num)
        solution += sub_sols
    cache[target] = solution
    return solution

def add_num(sub_sol, num):
    new_sol = []
    for lst in sub_sol:
        new_l = lst + [num]
        new_l = sorted(new_l)
        new_sol.append(new_l)
    return new_sol

print(combination_sum([2, 3, 5, 8], 8))
