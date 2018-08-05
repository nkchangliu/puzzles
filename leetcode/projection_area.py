def projection_area(matrix):
    if not matrix:
        return 0
    xy, yz, xz = 0, 0, 0

    for lst in matrix:
        for num in lst:
            if num != 0:
                xy += 1

    for lst in matrix:
        yz += max(lst)
    for i in range(len(matrix[0])):
        xz += find_max_col(matrix, i)
    return xy + yz + xz

def find_max_col(matrix, col):
    max_num = -float("inf")
    for i in range(len(matrix)):
        max_num = max(matrix[i][col], max_num)
    return max_num

print(projection_area([[2,2,2],[2,1,2],[2,2,2]]))
