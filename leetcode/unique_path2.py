def unique_path(grid):
    row = len(grid)
    col = len(grid[0])

    res = [[0 for i in range(col)] for j in range(row)]
    if grid[0][0] != 1:
        res[0][0] = 1
    for i in range(1, row):
        if grid[i][0] != 1 and res[i - 1][0] == 1:
            res[i][0] = 1
    for j in range(1, col):
        if grid[0][j] != 1 and res[0][j - 1] == 1:
            res[0][j] = 1

    for i in range(1, row):
        for j in range(1, col):
            if grid[i][j] == 1:
                res[i][j] = 0
            else:
                res[i][j] = res[i - 1][j] + res[i][j - 1]
    return res[-1][-1]


