def stone_game(lst):
    this, other = _stone_game(lst, 0, len(lst) - 1, {})
    return this > other

def _stone_game(lst, start, end, cache):
    if (start, end) in cache:
        return cache[(start, end)]

    if start == end:
        return lst[start], 0

    pick_start_this, pick_start_other = _stone_game(lst, start + 1, end, cache)
    pick_end_this, pick_end_other = _stone_game(lst, start, end - 1, cache)

    if pick_start_other + lst[start] >= pick_end_other + lst[end]:
        cache[(start, end)] =  pick_start_other + lst[start], pick_start_this
    else:
        cache[(start, end)] =  pick_end_other + lst[end], pick_end_this
    return cache[(start, end)]

print(stone_game([5, 3, 4, 5]))
