def max_chunk_sorted(lst):
    i, chunk = 0, 0
    while i < len(lst):
        j = lst[i]
        while j < len(lst) and not okay_chunk(lst, i, j):
            j = max(j, max(lst[i: j + 1]))
        chunk += 1
        i = j + 1
    return chunk

def okay_chunk(lst, i , j):
    for num in lst[i: j + 1]:
        if num < i or num > j:
            return False
    return True

