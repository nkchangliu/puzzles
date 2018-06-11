def pascal(num):
    if num == 0:
        return []
    elif num == 1:
        return [[1]]
    lst = [[1]]
    for i in range(1, num):
        new_lst = [1]
        for j in range(len(lst[-1]) - 1):
            new_lst.append(lst[-1][j] + lst[-1][j + 1])
        new_lst.append(1)
        lst.append(new_lst)
    return lst

print(pascal(5))
