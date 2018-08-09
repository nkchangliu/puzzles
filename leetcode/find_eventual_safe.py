WHITE, GRAY, BLACK = 0, 1, 2

def find_eventual_safe(lst):
    color = {}
    for i in range(len(lst)):
        color[i] = WHITE
    for i in range(len(lst)):
        if color[i] == WHITE:
            dfs(lst, i, color)

    return [x for x in color if color[x] != GRAY]

def dfs(lst, node, color):
    if color[node] == GRAY:
        return True
    else:
        color[node] = GRAY
        for successor in lst[node]:
            if color[successor] == BLACK:
                continue
            if color[successor] == GRAY or dfs(lst, successor, color):
                return True
        color[node] = BLACK
    return False

print(find_eventual_safe([[1,2],[2,3],[5],[0],[5],[],[]]))

