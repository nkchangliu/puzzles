import heapq
def custom_sort(s, t):
    map = {k : v for v, k in enumerate(s)}
    q = []

    for c in t:
        heapq.heappush(q, (map[c] if c in map else float("inf"), c))

    res = []
    while q:
        _, c = heapq.heappop(q)
        res.append(c)
    return "".join(res)

print(custom_sort("cba", "abbcd"))



