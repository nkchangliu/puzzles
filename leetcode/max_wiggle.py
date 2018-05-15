def max_wiggle(lst):
    if len(lst) < 2:
        return len(lst)
    start = 0
    max_length = 0
    while start < len(lst) - 1:
        length, start = max_wiggle_start(lst, start)
        if length > max_length:
            max_length = length
    return max_length


def max_wiggle_start(lst, start):
    if lst[start] == lst[start + 1]:
        return 1, start + 1
    end = start + 1

    while end + 1 < len(lst) and \
            ((lst[end + 1] < lst[end] and lst[end] > lst[end - 1]) or (lst[end + 1] > lst[end] and lst[end] < lst[end - 1])):
                end += 1
                print(end)
    return end - start + 1, end + 1


print(max_wiggle([1,17,5,10,13,15,10,5,16,8]))
