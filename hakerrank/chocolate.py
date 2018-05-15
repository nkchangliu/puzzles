# Have number in a lst = [1, 2, 3, 7, 4, 5]
# want to use m amount of num in lst such that sum to d.
# how many ways are there


def calculate_sum(lst, m, d):
    return calculate(lst, m, d)


def calculate(lst, m, d):
    w = 0
    if m == 0 and d == 0:
        return 1

    for num in lst:
        if num <= d:
            new_lst = [i for i in lst]
            new_lst.remove(num)
            w += calculate(new_lst, m - 1, d - num)

    return w



