# return true if only the number's prime factors are only 2, 3, 5

def is_ugly(num):
    if num == 0:
        return False
    while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        if num % 2 == 0:
            num = num // 2
        if num % 3 == 0:
            num = num // 3
        if num % 5 == 0:
            num = num // 5
    return num == 1


