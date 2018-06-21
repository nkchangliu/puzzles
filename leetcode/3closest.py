
def closest(lst, target):
    diff = float("inf")
    value = 0
    lst = sorted(lst)

    for i in range(len(lst) - 2):
        start = i + 1
        end = len(lst) - 1
        while start < end:
            curr_value = lst[i] + lst[start] + lst[end]
            if abs(target - curr_value) < diff:
                diff = abs(target - curr_value)
                value = curr_value
            if curr_value < target:
                start += 1
            elif curr_value == target:
                return target
            else:
                end -= 1
    return value


print(closest([-1, 2, 1, -4], 1))
