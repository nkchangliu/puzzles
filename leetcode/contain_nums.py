# check if a list has two distant value that are no more than t apart and the index is no more then k apart

def contain_nums(nums, k, t):
    num_dict = {}
    for counter, num in enumerate(nums):
        if num not in num_dict:
            num_dict[num] = []
        num_dict[num].append(counter)

    for key in num_dict:
        index = sorted(num_dict[key])
        for num in range(key, key + t + 1):
            if num in num_dict:
                next_index = sorted(num_dict[num])
                if with_in_range(index, next_index, k):
                    return True
    return False

def with_in_range(index, next_index, k):
    i, j = 0, 0
    while i < len(index) and j < len(next_index):
        if abs(index[i] - next_index[j]) <= k and index[i] != next_index[j]:
            return True
        elif index[i] > index[j]:
            j += 1
        else:
            i += 1
    return False


print(contain_nums([2, 1], 1, 1))
