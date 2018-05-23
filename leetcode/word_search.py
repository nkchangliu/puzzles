# given a string and a board, check if the string can be represented using sequential char in the board

def word_search(s, board):
    seed_paths = find_seed_path(s, board)

    for seed_path in seed_paths:
        if _valid_path(s, board, seed_path):
            return True

    return False

def _valid_path(s, board, seed_path):
    lst = [seed_path]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while lst:

        path = lst.pop()
        if len(path) == len(s):
            return True

        path_r, path_c = path[-1]
        for change_r, change_c in directions:

            if is_valid(path_r + change_r, path_c + change_c, board) \
                and (path_r + change_r, path_c + change_c) not in path \
                and board[path_r + change_r][path_c + change_c] == s[len(path)]:
                    new_path = path + [(path_r + change_r, path_c + change_c)]
                    lst.append(new_path)
    return False

def find_seed_path(s, board):
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == s[0]:
                res.append([(i, j)])
    return res

def is_valid(row, col, board):
    return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

