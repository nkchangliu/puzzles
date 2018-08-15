def partition_equal_sum(lst, k):
    total = sum(lst)
    if total % k != 0:
        return False
    visited = set()
    return can_partition(lst, visited, k, 0, 0, total // k)

def can_partition(lst, visited, k, curr_sum, curr_ind, target):
    if k == 1: return True
    if curr_sum == target:
        return can_partition(lst, visited, k - 1, 0, 0, target)
    for i in range(curr_ind, len(lst)):
        if i not in visited:
            visited.add(i)
            if can_partition(lst, visited, k, curr_sum + lst[i], i + 1, target):
                return True
            visited.remove(i)
    return False

