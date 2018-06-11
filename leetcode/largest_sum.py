def largest_sum(lst, k):
    memo = {}
    return search(lst, len(lst), k, memo)

def search(lst, n, k, memo):
    if (n, k) in memo:
        return memo[(n, k)]
    elif n < k:
        return 0
    elif n == k:
        memo[(n, k)] = sum(lst[:n])
    elif k == 1:
        memo[(n, k)] = sum(lst[:n]) / float(n)
    else:
        count, memo[(n, k)] = 0, 0
        for i in range(n - 1, 0, -1):
            count += lst[i]
            memo[(n, k)] = max(memo[n, k], search(lst, i, k - 1, memo) + count / float(n - i))
    return memo[(n, k)]



print(largest_sum([9, 1, 2, 3, 9], 3))
