def num_occur(first, second):
    count = 0
    for i in range(len(first) - len(second) + 1):
        if first[i : i + len(second)] == second:
            count += 1
    return count

def num_occur_no_overlap(first, second):
    i, count = 0, 0
    while i < len(first) - len(second) + 1:
        if first[i : i+len(second)] == second:
            count += 1
            i += len(second)
        else:
            i += 1
    return count

print(num_occur_no_overlap('aaa','aa'))
