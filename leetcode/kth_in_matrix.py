import math

def kth_in_matrix(matrix, k):
    ind = int(math.floor(k ** 0.5))
    if ind == k ** 0.5:
        return matrix[ind - 1][ind - 1]

    num_left = k - ind ** 2
    row, col = 0, 0
    while row < len(matrix) - 1 and col < len(matrix) - 1:
        num_left -= 1
        if matrix[col][ind] < matrix[ind][row]:
            if num_left == 0:
                return matrix[col][ind]
            col += 1
        else:
            if num_left == 0:
                return matrix[ind][row]
            row += 1
    if row < len(matrix) - 1:
        return matrix[ind][row + num_left - 1]
    else:
        return matrix[col + num_left - 1][ind]


print(kth_in_matrix([[1,3,5],[6,7,12],[11,14,14]], 3))
