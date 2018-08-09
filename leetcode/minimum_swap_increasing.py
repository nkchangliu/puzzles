def minimum_swap(a, b):
    move = [float("inf")] * len(a)
    not_move = [float("inf")] * len(a)
    last_pair_move = b[0], a[0]
    last_pair_not_move = a[0], b[0]
    move[0] = 1
    not_move[0] = 0
    for i in range(1, len(a)):
        a_num = a[i]
        b_num = b[i]

        not_move[i] = update(a_num, b_num, last_pair_move, last_pair_not_move, move, not_move, i)
        move[i] = update(b_num, a_num, last_pair_move, last_pair_not_move,move, not_move, i) + 1

        last_pair_not_move = a_num, b_num
        last_pair_move = b_num, a_num
    return min(move[-1], not_move[-1])

def update(num1, num2, pair_move, pair_not_move, move, not_move, i):
    if larger(num1, num2,pair_move) and larger(num1, num2, pair_not_move):
        return min(not_move[i - 1], move[i - 1])
    elif larger(num1, num2, pair_move):
        return move[i - 1]
    elif larger(num1, num2, pair_not_move):
        return not_move[i - 1]
    return float("inf")

def larger(num1, num2, pair):
    return num1 > pair[0] and num2 > pair[1]

print(minimum_swap([1, 3, 5, 4], [1, 2, 3, 7]))
