
def longest_fib(lst):
    nums = set(lst)
    checked = set()
    res = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            first = lst[i]
            second = lst[j]
            longest = 0
            while first + second in nums and not (first, second) in checked:
                checked.add((first, second))
                longest += 1
                first, second = second, first + second
            res = max(res, longest)
    return res + 2 if res else 0

