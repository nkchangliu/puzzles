def maximal_square(matrix):
    max_square = 0
    for num_row, num_col in get_one(matrix):
        square = get_big_square(matrix, num_row, num_col)
        if square > max_square:
            max_square = square
    return max_square ** 2


def get_one(matrix):
    lst = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                lst.append((row, col))
    return lst


def get_big_square(matrix, num_row, num_col):
    length = min(len(matrix) - num_row, len(matrix) - num_col)
    i = 1
    while i < length:
        ok = True
        max_row = num_row + i
        max_col = num_col + i
        for row in range(num_row, num_row + i + 1):
            if matrix[row][num_col+i] != 1:
                ok = False
        for col in range(num_col, num_col+i + 1):
            if matrix[num_row+i][col] != 1:
                ok = False
        if not ok:
            break
        else:
            i += 1
    return i


matrix = [[1, 0, 1, 0, 0],[1, 0, 1, 1, 1],[1, 1, 1, 1, 1],[1, 0, 0, 1, 0]]

print(maximal_square(matrix))

