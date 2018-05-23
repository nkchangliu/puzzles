import math

def find_count(num):
    lst = [i ** 2 for i in range(1, int(math.sqrt(num)) + 1)]
    cache = {}
    cache[0] = 0
    return perfect_square(num, cache, lst)

def perfect_square(num, cache, lst):
    if num in cache:
        return cache[num]
    min_val = None
    for seed in reversed(lst):
        if num - seed >= 0:
            val = perfect_square(num-seed, cache, lst)
            if min_val is None or val < min_val:
                min_val = val
    cache[num] = min_val + 1
    return cache[num]

print(find_count(20))
