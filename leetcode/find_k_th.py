from random import randint
def find_k_th(lst, k):
    pivot =randint(0, len(lst) - 1)
    smaller = [num for num in lst if num < lst[pivot]]
    same = [num for num in lst if num == lst[pivot]]
    large = [num for num in lst if num > lst[pivot]]
    if len(large) >= k:
        return find_k_th(large, k)
    elif len(large) + len(same) >= k:
        return same[0]
    else:
        return find_k_th(smaller, k - len(large) - len(same))

print(find_k_th([3,4,2, 5, 6, 1, 7, 3, 6, 5 ,8, 9], 3))
