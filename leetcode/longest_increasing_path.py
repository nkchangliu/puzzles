def longest_path_increasing(matrix):
    cache = {}
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res = max(res, helper(matrix, i, j, cache))
    return res

def helper(matrix, i, j, cache):
    if (i, j) in cache:
        return cache[(i, j)]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    sub_res = 0
    for dir_r, dir_c in directions:
        new_r, new_c = i + dir_r, j + dir_c
        if inside(matrix, new_r, new_c) and matrix[new_r][new_c] < matrix[i][j]:
            sub_res = max(sub_res, helper(matrix, new_r, new_c, cache))
    cache[(i, j)] = sub_res + 1
    return cache[(i, j)]

def inside(matrix, new_r, new_c):
    return new_r >= 0 and new_r < len(matrix) and new_c >= 0 and new_c < len(matrix[0])


print(longest_path_increasing([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))


