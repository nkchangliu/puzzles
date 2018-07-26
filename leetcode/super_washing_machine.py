def super_washing_machine(lst):
    if sum(lst) % len(lst) != 0:
        return -1
    avg = sum(lst) // len(lst)

    max_diff, pass_diff = 0, 0
    for num in lst:
        pass_diff += avg - num
        max_diff = max(max(max_diff, abs(pass_diff), num - avg)
    return max_diff
