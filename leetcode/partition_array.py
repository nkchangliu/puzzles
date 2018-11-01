def get_left_size(A):
    left_large = [A[0]]
    for i in range(0, len(A)-1):
        left_large.append(max(A[i], left_large[-1]))
    right_small = [A[-1]]
    for i in reversed(range(len(A) - 1)):
        right_small.append(min(right_small[-1], A[i]))
    right_small = right_small[::-1]
    print(left_large)
    print(right_small)
    for i in range(len(left_large)):
        if left_large[i] <= right_small[i]:
            return max(1, i)

print(get_left_size([1,1,1,0,6,12]))
