def get_number(target):
    res = []
    for i in range(1, 10):
        res += _get_number(i, target)
    return res

def _get_number(i, target):
    if i > target: return []
    else:
        sub_res = [i]
        for j in range(10):
            if 10 * i + j <= target:
                sub_res += _get_number(10 * i + j, target)
    return sub_res

print(get_number(13))


