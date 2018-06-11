def valid_sub(lst, low, high):
    curr_index = 0
    res = 0
    num_sub = 0

    for i in range(len(lst)):
        if lst[i] >= low and lst[i] <= high:
            res += i - curr_index + 1
            num_sub = i - curr_index + 1
        elif lst[i] < low:
            res += num_sub
        else:
            curr_index = i + 1
            num_sub = 0
    return res

print(valid_sub([2, 1, 4, 3], 2, 3))
