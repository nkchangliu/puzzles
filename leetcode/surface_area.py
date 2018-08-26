def surface_area(lst):
    up = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j]:
                up += 1
    side = get_area(lst)
    return 2 * up + side

def get_area(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            res += get_value(lst, i, j)
    return res

def get_value(lst, i, j):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = 0
    for d_r, d_c in dirs:
        if is_valid(lst, d_r + i, d_c + j):
            res += max(0, lst[i][j] - lst[d_r + i][d_c + j])
        else:
            res += lst[i][j]
    return res

def is_valid(lst, r, c):
    return r >= 0 and r <len(lst) and c >= 0 and c < len(lst[0])


print(surface_area([[2]]))
