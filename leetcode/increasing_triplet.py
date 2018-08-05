def increasing_triplet(lst):
    if not lst:
        return False
    left_small = [float("inf")]

    for num in lst:
        if num < left_small[-1]:
            left_small.append(num)
        else:
            left_small.append(left_small[-1])

    largest = lst[-1]

    for i in range(len(lst) - 2, 0, -1):
        if lst[i] < largest and lst[i] > left_small[i]:
            return True
        largest = max(largest, lst[i])

    return False



print(increasing_triplet([4, 2, 1, 5, 2, 1]))

