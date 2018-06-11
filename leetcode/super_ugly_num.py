def super_ugly_num(primes, n):
    res = [1]
    index = [0] * len(primes)
    while len(res) < n:
        value = find_min(primes, index, res)
        res.append(value)
    print(res)
    return res[n - 1]

def find_min(primes, index, res):
    value = None
    for i in range(len(primes)):
        if value is None or primes[i] * res[index[i]] < value:
            smallest = set()
            value = primes[i] * res[index[i]]
            smallest.add(i)
        elif primes[i] * res[index[i]] == value:
            smallest.add(i)

    for i in smallest:
        index[i] += 1
    return value

print(super_ugly_num([2, 7, 13, 19], 12))
