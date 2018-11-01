
def max_subarray(A):
    non_circular =  _max_sum(A)
    circular = sum(A) - min(0, _min_sum(A))
    if circular == 0:
        return non_circular
    return max(non_circular, circular)
def _min_sum(A):
    include = not_include = float("inf")
    for num in A:
        not_include = min(include, not_include)
        # include
        include = min(num, num + include)
    return min(include, not_include)

def _max_sum(A):
    include = not_include = -float("inf")
    for num in A:
        not_include = max(include, not_include)
        # include
        include = max(num, num + include)
    return max(include, not_include)
print(max_subarray([5, -3, 5]))
print(max_subarray([3, -1, 2, -1]))
print(max_subarray([3, -2, 2, -3]))
print(max_subarray([-2, -3, -1]))
