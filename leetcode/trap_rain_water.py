def rain_water(lst):
    return trap_water(lst, 0, len(lst) - 1)

def trap_water(lst, start, end):
    if start + 1 >= end:
        return 0

    high_l, high_h = find_highest_two(lst, start, end)
    return trap_water(lst, start, high_l) + trap_water(lst, high_h, end) + amount_between(lst, high_l, high_h)


def find_highest_two(lst, start, end):
    high_f, high_s = None, None
    for i in range(start, end + 1):
        if high_f is None or lst[i] > lst[high_f]:
            high_f, high_s = i, high_f
        elif high_s is None or lst[i] > lst[high_s]:
            high_s = i
    return min(high_f, high_s), max(high_f, high_s)


def amount_between(lst, high_l, high_h):
    low_amount = min(lst[high_l], lst[high_h])
    amount = 0
    for i in range(high_l + 1, high_h):
        if lst[i] < low_amount:
            amount += low_amount - lst[i]
    return amount

print(rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
