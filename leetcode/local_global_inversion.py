def local_global_inversion(lst):
    for i in range(len(lst)):
        if abs(lst[i] - i) > 1:
            return False
    return True

