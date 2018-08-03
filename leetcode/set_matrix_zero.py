def set_matrix_zero(matrix):
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)

    for i in row:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0

    for j in col:
        for i in range(len(matrix)):
            matrix[i][j] = 0

ZERO = "change_zero"
def set_matrix_zero_no_mem(matrix):
    first_col = False
    first_row = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i == 0 and j == 0:
                    first_col = True
                    first_row = True
                elif j != 0 and i != 0:
                    matrix[i][0] = ZERO
                    matrix[0][j] = ZERO
                elif j == 0:
                    first_col = True
                    matrix[i][0] = ZERO
                else:
                    first_row = True
                    matrix[0][j] = ZERO
    print(matrix)
    for i in range(len(matrix)):
        if matrix[i][0] == ZERO:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    for j in range(len(matrix[0])):
        if matrix[0][j] == ZERO:
            for i in range(len(matrix)):
                matrix[i][j] = 0
    if first_col:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    if first_row:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    return matrix

print(set_matrix_zero_no_mem([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
