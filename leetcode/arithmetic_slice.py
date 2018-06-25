def arithmetic_slice(lst):
    if len(lst) < 3:
        return 0
    last_count, total = 0, 0
    if lst[1] - lst[0] == lst[2] - lst[1]:
        last_count = 1
        total = last_count
    for i in range(3, len(lst)):
        if lst[i] - lst[i - 1] == lst[i - 1] - lst[i - 2]:
            new_count = 1 + last_count
            total += new_count
            last_count = new_count
        else:
            last_count = 0

    return total

print(arithmetic_slice([1, 2, 3, 4, 7, 8, 9]))



