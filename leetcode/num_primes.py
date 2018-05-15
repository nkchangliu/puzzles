
def find_prime(n):
    if n <= 2:
        return 0
    lst = [True] * n
    lst[0], lst[1] = False, False

    for i in range(2, n):
        if lst[i] == True:
            for j in range(2, (n-1)//i+1):
                lst[i * j] = False
    return sum(lst)


