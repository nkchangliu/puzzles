def check_pattern(lst):
    min_num = float("inf")
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j] and min_num < lst[j]:
                return True
        min_num = min(min_num, lst[i])
    return False

print(check_pattern([3, 1, 4, 2]))

