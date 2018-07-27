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


def maximal_square_dp(matrix):
    max_len = 0
    res = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix[0])):
        res[0][i] = matrix[0][i]
        max_len = max(max_len, res[0][i])
    for i in range(len(matrix)):
        res[i][0] = matrix[i][0]
        max_len = max(max_len, res[i][0])
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                res[i][j] = 0
            else:
                res[i][j] = min(res[i-1][j], res[i][j - 1], res[i - 1][j - 1]) + 1
            max_len = max(max_len, res[i][j])
    return max_len ** 2

matrix = [[1, 0, 1, 0, 0],[1, 0, 1, 1, 1],[1, 1, 1, 1, 1],[1, 0, 0, 1, 0]]

print(maximal_square_dp(matrix))

