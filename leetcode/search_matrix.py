def search_matrix(matrix, target):
    if len(matrix) < 1 or len(matrix[0]) < 1:
        return False

    i, j = 0, len(matrix[0]) - 1
    while i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]):
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
        else:
            return True
    return False

print(search_matrix([[-1],[-1]], 0))

print(search_matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 19))
