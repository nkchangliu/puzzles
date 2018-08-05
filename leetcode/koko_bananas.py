def calculate_time(lst, mid):
    total_hour = 0
    for num in lst:
        total_hour += math.ceil(num / mid)
    return total_hour


def koko_bananas(lst, hour):
    start, end = 1, max(lst)
    while start < end:
        mid = (start + end) // 2
        if calculate_time(lst, mid) > hour:
            start = mid + 1
        else:
            end = mid
    return start


