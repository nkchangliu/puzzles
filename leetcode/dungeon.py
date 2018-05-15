def minimum_hp(dungeon):
    row, col = len(dungeon), len(dungeon[0])
    hp = [[None for i in range(col)] for j in range(row)]

    hp[-1][-1] = max(1, 1-dungeon[-1][-1])

    for i in range(row-2, -1, -1):
        hp[i][-1] = max(hp[i+1][-1] - dungeon[i][-1], 1)

    for j in range(col-2, -1, -1):
        hp[-1][j] = max(hp[-1][j+1] - dungeon[-1][j], 1)

    for i in range(row-2, -1, -1):
        for j in range(col-2, -1, -1):
            hp[i][j] = max(min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j], 1)

    return hp[0][0]

print(minimum_hp([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
