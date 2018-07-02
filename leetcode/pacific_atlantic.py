def pacific_atlantic(matrix):
    row = len(matrix)
    col = len(matrix[0])

    to_visit_p, to_visit_a = [], []
    for i in range(row):
        to_visit_p.append((i, 0))
        to_visit_a.append((i, col - 1))
    for i in range(col):
        to_visit_p.append((0, i))
        to_visit_a.append((row - 1, i))

    can_reach_p = DFS(matrix, to_visit_p)
    can_reach_a = DFS(matrix, to_visit_a)

    res = []
    for pos in can_reach_p:
        if pos in can_reach_a:
            res.append(pos)
    return res

def DFS(matrix, to_visit):
    visited = set()
    while to_visit:
        next_pos = to_visit.pop()
        visited.add(next_pos)
        for successor in get_successor(matrix, next_pos):
            if successor not in visited and successor not in to_visit:
                to_visit.append(successor)
    return visited

def get_successor(matrix, pos):
    successor = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for direction in directions:
        new_pos_row, new_pos_col = pos[0] + direction[0], pos[1] + direction[1]
        if new_pos_row >= 0 and new_pos_row < len(matrix) and new_pos_col >= 0 and new_pos_col < len(matrix[0]):
            if matrix[new_pos_row][new_pos_col] >= matrix[pos[0]][pos[1]]:
                successor.append((new_pos_row, new_pos_col))
    return successor

matrix = [[8,13,11,18,14,16],[2,9,15,16,14,5],[15,16,17,10,3,6]]
print(pacific_atlantic(matrix))





