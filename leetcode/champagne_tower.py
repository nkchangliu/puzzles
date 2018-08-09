def tower(amount, row, col):
    if row == 0:
        return min(amount, 1)

    leftover = [max(amount - 1, 0)]
    last_row = [1]
    for i in range(1, row + 1):
        value = min(leftover[0] /2, 1)
        new_leftover = [max(leftover[0]/2 - 1, 0)]
        if i == row and (col == 0 or col  == len(leftover)):
            return value
        for j in range(1, len(leftover)):
            value = min((leftover[j] + leftover[j - 1])/ 2, 1)
            new_leftover.append(max((leftover[j] + leftover[j - 1]) / 2 - 1, 0))
            if i == row and j == col:
                return value
        new_leftover.append(max(leftover[0]/2 - 1, 0))
        leftover = new_leftover

print(tower(4, 3, 1))
