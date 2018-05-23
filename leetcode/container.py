def most_water(lst):
    i, j = 0, len(lst) - 1
    max_contain = 0
    while i < j:
        contain = (j - i) * min(lst[i], lst[j])
        if contain > max_contain:
            max_contain = contain
        if lst[i] > lst[j]:
            j -= 1
        else:
            i += 1
    return max_contain

print(most_water([1, 4, 5, 3, 2, 4, 6, 1]))


