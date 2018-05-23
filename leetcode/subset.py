# given a list of numbers return all the possible sets

def subset(lst):
    res = [[]]
    for num in sorted(lst):
        print(res)
        res += [item + [num] for item in res]

    return res

print(subset([1, 2, 3]))
