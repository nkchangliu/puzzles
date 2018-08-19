def subsequence_sum(lst):
    if len(lst) < 2:
        return 0
    lst.sort()
    last_count = 1
    old_val = lst[1] - lst[0]
    total = old_val
    old_two = 1 # 2 ^ 0

    for i in range(2, len(lst)):
        diff = lst[i] - lst[i - 1]
        old_two *= 2
        new_count = last_count + old_two
        new_val = new_count * diff + 2 * old_val
        total = (total + new_val) % (10**9 + 7)
        old_val, last_count = new_val, new_count
    return total

print(subsequence_sum([4, 7, 8, 8, 10]))
