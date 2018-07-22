import heapq
def find_k_smallest(pairs, k):
    pairs = sorted(pairs)
    q = []
    added = set()
    for i in range(len(pairs) - 1):
        heapq.heappush(q, (pairs[i + 1] - pairs[i], (i, i + 1)))
        added.add((i, i + 1))
    num = 0

    while q and num < k:
        item_prio, (start, end) = heapq.heappop(q)
        num += 1
        if start - 1 >= 0 and (start - 1, end) not in added:
            heapq.heappush(q, (pairs[end] - pairs[start - 1], (start - 1, end)))
            added.add((start - 1, end))
        if end + 1 < len(pairs) and (start, end + 1) not in added:
            heapq.heappush(q, (pairs[end + 1] - pairs[start], (start, end + 1)))
            added.add((start, end + 1))
    return item_prio

print(find_k_smallest([1, 1, 3, 4], 5))

