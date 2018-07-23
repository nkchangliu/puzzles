def power_of_two(num):
    power_lst = [str(2 **i) for i in range(30)]
    for s in power_lst:
        if sorted(s) == sorted(str(num)):
            return True
    return False
