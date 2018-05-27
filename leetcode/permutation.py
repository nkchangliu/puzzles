def permutation(lst):
    past = [[]]

    for num in lst:
        curr = []
        for p in past:
            for i in range(len(p) + 1):
                new_p = p[0:i] + [num] + p[i:]
                curr.append(new_p)
        past = curr
    return past

print(permutation([1, 2, 3]))
