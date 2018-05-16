# find the shortest subarray that need to be sorted inorder to be non decreasing

def shorted_subarray(lst):
    sorted_lst = sorted(lst)
    if lst == sorted_lst:
        return 0
    count = 0
    for i in range(len(lst)):
        if lst[i] == sorted_lst[i]:
            count += 1
        else:
            break
    for j in reversed(range(len(lst))):
        if lst[j] == sorted_lst[j]:
            count += 1
        else:
            break
    return len(lst) - count


