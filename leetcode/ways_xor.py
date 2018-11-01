def ways_xor(A):
    if not A: return 0
    ways_at_ind = {}
    ways_at_ind[0] = set()
    ways_at_ind[0].add(A[0])
    for i in range(1, len(A)):
        old_ways = ways_at_ind[i - 1]
        curr_ways = set()
        curr_ways.add(A[i])
        for xor_val in old_ways:
            curr_ways.add(xor_val | A[i])
        ways_at_ind[i] = curr_ways
    total_ways = set()
    print(ways_at_ind)
    for key in ways_at_ind:
        total_ways.update(ways_at_ind[key])
    return len(total_ways)

print(ways_xor([1, 2, 4]))
