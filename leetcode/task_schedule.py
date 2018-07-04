from collections import Counter
def task_schedule(lst, idle):
    counts = Counter(lst)
    max_count = max(counts.values())
    total = (idle + 1) * (max_count - 1) + 1
    num_of_max = 0
    for count in counts.values():
        if count == max_count:
            num_of_max += 1
    total += num_of_max - 1
    return max(total, len(lst))

print(task_schedule(["A","A","A","A","A","A","B","C","D","E","F","G"],2))

