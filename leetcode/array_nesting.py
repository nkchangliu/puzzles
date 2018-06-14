def array_nesting(lst):
    visited = set()
    max_count = 0
    for num in lst:
        if num not in visited:
            max_count = max(max_count, calculate_max(lst, num, visited))
    return max_count

def calculate_max(lst, num, visited):
    count = 0
    while lst[num] not in visited:
        num = lst[num]
        count += 1
        visited.add(num)
    return count

print(array_nesting([5,4,0,3,1,6,2]))
