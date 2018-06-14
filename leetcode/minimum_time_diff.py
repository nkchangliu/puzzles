def minimum_time(lst):
    buckets = [False] * (24 * 60)

    for time in lst:
        hour_mins = time.split(":")
        minutes = 60 * int(hour_mins[0]) + int(hour_mins[1])

        if buckets[minutes]:
            return 0
        else:
            buckets[minutes] = True
    min_value = float('inf')
    prev, first, last = None, None, None
    for i in range(len(buckets)):
        if buckets[i]:
            if prev is not None and i - prev < min_value:
                min_value = i - prev
            prev = i
            if first is None:
                first = i
            if last is None or i > last:
                last = i

    return min(min_value, (24* 60 - last + first))

print(minimum_time(["23:59","00:00"]))
