def spiral(matrix):
    if not matrix:
        return []
    elif len(matrix) == 1:
        return matrix[0]
    elif len(matrix[0]) == 1:
        res = []
        for lst in matrix:
            res += lst
        return res

    res = []
    for num in matrix[0]:
        res.append(num)
    for i in range(1, len(matrix) - 1):
        res.append(matrix[i][len(matrix[0]) - 1])
    for i in reversed(range(0, len(matrix[0]))):
        res.append(matrix[len(matrix) - 1][i])
    for i in reversed(range(1, len(matrix) -1)):
        res.append(matrix[i][0])
    return res + spiral(inner_matrix(matrix))

def inner_matrix(matrix):
    res = []
    for i in range(1, len(matrix) -1):
        row = []
        for j in range(1, len(matrix[0]) - 1):
            row.append(matrix[i][j])
        if row:
            res.append(row)
    return res

print(spiral([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))
