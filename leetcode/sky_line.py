def sky_line(grid):
    row_max = [max(row) for row in grid]
    col_max = [max(col) for col in zip(*grid)]
    print(row_max)
    print(col_max)
    max_amount = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            max_amount += min(row_max[i], col_max[j]) - grid[i][j]
    return max_amount

print(sky_line([[59,88,44],[3,18,38],[21,26,51]]))
