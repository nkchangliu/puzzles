from queue import Queue

def shortest_path(grid):
    start, count_keys = find_start(grid)

    need_to_visit = Queue()
    need_to_visit.put((start, "", 0))
    moves_dict = {}
    moves_dict[(start, "")] = 0

    while need_to_visit.qsize() > 0:
        print(list(need_to_visit.queue))
        (node, keys, moves) = need_to_visit.get()
        for (successor, successor_keys, successor_moves) in get_successor(grid, node, keys, moves):
            if len(successor_keys) == count_keys:
                return successor_moves
            elif (successor, successor_keys) not in moves_dict:
                need_to_visit.put((successor, successor_keys, successor_moves))
                moves_dict[(successor, successor_keys)] = successor_moves
    return -1

def find_start(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                start = i, j
            if grid[i][j].islower():
                count += 1
    return start, count

def get_successor(grid, node, keys, moves):
    successors = []
    node_x, node_y = node[0], node[1]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction_x, direction_y in directions:
        next_x, next_y = node_x + direction_x, node_y + direction_y
        if next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]):
            if grid[next_x][next_y] == "." or grid[next_x][next_y] == "@":
                successors.append(((next_x, next_y), keys, moves + 1))
            elif grid[next_x][next_y].islower():
                if grid[next_x][next_y] not in keys:
                    new_keys = ''.join(sorted(keys + grid[next_x][next_y]))
                    successors.append(((next_x, next_y), new_keys, moves + 1))
                else:
                    successors.append(((next_x, next_y), keys, moves + 1))

            elif grid[next_x][next_y].isupper():
                upper_char = grid[next_x][next_y]
                if upper_char.lower() in keys:
                    successors.append(((next_x, next_y), keys, moves + 1))
    return successors


print(shortest_path(["@.a.#","###.#","b.A.B"]))
