def median_lst(a, b):
    if len(a) > len(b):
        a, b = b, a
    start = 0
    end = len(a)
    while start <= end:
        i = (start + end) // 2
        j = (len(a) + len(b) + 1) // 2 - i
        if i > 0 and a[i - 1] > b[j]:
            end = i - 1
        elif i < len(a) and b[j - 1] > a[i]:
            start = i + 1
        else:
            if i == 0: max_left = b[j-1]
            elif j == 0: max_left = a[i-1]
            else: max_left = max(a[i-1], b[j-1])

            if (len(a) + len(b)) % 2 == 1:
                return max_left

            if i == len(a): min_right = b[j]
            elif j == len(b): min_right = a[i]
            else: min_right = min(a[i], b[j])

            return (max_left + min_right) / 2

print(median_lst([1, 2, 3, 4], [2, 3, 4]))
