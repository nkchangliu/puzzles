def smallest_range(A, K):
    if len(A) <= 1:
        return 0
    A.sort()
    min_num = max_num = A[0] + K
    for i in range(1, len(A)):
        plus_k = A[i] + K
        minus_k = A[i] - K
        if abs(plus_k - min_num) <= abs(minus_k - max_num):
            #choose plus_k
            min_num = min(plus_k, min_num)
            max_num = max(plus_k, max_num)
        else:
            min_num = min(minus_k, min_num)
            max_num = max(minus_k, max_num)
    return max_num - min_num

print(smallest_range([1, 4, 8, 10],3))
