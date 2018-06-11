def keys_n_rooms(lst):
    if not lst:
        return True
    visited = set()
    can_visit = []
    visited.add(0)
    can_visit += lst[0]
    while can_visit:
        v = can_visit.pop()
        visited.add(v)
        if len(visited) == len(lst):
            return True
        for key in lst[v]:
            if key not in visited and key not in can_visit:
                can_visit.append(key)
    return len(visited) == len(lst)

print(keys_n_rooms([[]]))


