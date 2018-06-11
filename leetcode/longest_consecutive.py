def longest_consecutive(lst):
    if not lst:
        return 0
    num_set = set(lst)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr_num = num
            curr_len = 1
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_len += 1
            if curr_len > longest:
                longest = curr_len
    return longest
