def min_path_sum(grid):
    row = len(grid)
    col = len(grid[0])
    res = [[None for i in range(col)] for j in range(row)]
    res[0][0] = grid[0][0]

    for j in range(1, col):
        res[0][j] = grid[0][j] + res[0][j -1]

    for i in range(1, row):
        res[i][0] = res[i - 1][0] + grid[i][0]

    for i in range(1, row):
        for j in range(1, col):
            res[i][j] = grid[i][j] + min(res[i-1][j], res[i][j-1])
    return res[row - 1][col -1]


print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
