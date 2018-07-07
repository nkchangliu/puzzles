def valid_sudoku(grid):
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        if not valid_row(grid, i):
            return False

    for i in range(col):
        if not valid_col(grid, i):
            return False

    for start_row in [0, 3, 6]:
        for start_col in [0, 3, 6]:
            if not valid_square(grid, start_row, start_col):
                return False
    return True

def check_num(num, cache):
    if num.isdigit():
        num = int(num)
        if num < 1 or num > 9 or num in cache:
            return False
        cache.add(num)
    return True

def valid_row(grid, row):
    cache = set()
    for num in grid[row]:
        if not check_num(num, cache):
            return False
    return True

def valid_col(grid, col):
    cache = set()
    for i in range(len(grid)):
        num = grid[i][col]
        if not check_num(num, cache):
            return False
    return True

def valid_square(grid, start_row, start_col):
    cache = set()
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            num = grid[i][j]
            if not check_num(num, cache):
                return False
    return True


