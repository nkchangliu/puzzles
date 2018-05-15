# count the unique path from top-left to bottom-right of a grid

def unique_path(m, n):
    res = [[1 for i in range(n)] for j in range(m)]

    for i in range(1, m):
        for j in range(1, n):

            res[i][j] = res[i - 1][j] + res[i][j - 1]

    return res[m - 1][n - 1]

print(unique_path(3, 2))
