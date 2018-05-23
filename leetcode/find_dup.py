# given a list that is len n and contains number 1-n with one duplicate
# number, find that duplicate number

def find_dup(lst):
    low = 1
    high = len(lst)
    while low < high:
        mid = low + (high - low) // 2
        count = 0

        for num in lst:
            if num <= mid:
                count += 1

        if count <= mid:
            low = mid + 1
        else:
            high = mid
    return low

print(find_dup([1, 1, 2, 3, 4]))

