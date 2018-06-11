def gas_station(gas, cost):
    cache = {}
    lst = []

    for i in range(len(gas)):
        cache[(i, (i + 1)% len(gas))] = gas[i] - cost[i]
        if gas[i] - cost[i] >= 0:
            lst.append((i, (i + 1)% len(gas)))

    while lst:
        start, end = lst.pop()
        if start == end:
            return start
        new_end = (end + 1) % len(gas)
        cost = cache[(start, end)] + cache[(end, new_end)]
        cache[(start, new_end)] = cost
        if cost >= 0:
            lst.append((start, new_end))
    return -1


def gas_station_2(gas, cost):
    total, min_total, min_ind = 0, gas[0] - cost[0], 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < min_total:
            print('lol')
            min_total = total
            min_ind = i
    if total < 0:
        return -1
    else:
        return (min_ind + 1) % len(gas)

print(gas_station_2([3,1,1], [1,2,2]))
