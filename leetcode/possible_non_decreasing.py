# check if a list can become a nondecreasing by modifying one element in the list

def check_non_decreasing(lst):
    count = 0
    index = 0
    for i in range(len(lst) -1):
        if lst[i] > lst[i + 1]:
            count += 1
            index = i
        if count > 1:
            return False

    if index > 0 and index < len(lst) - 2 \
            and lst[index] > lst[index + 2] and lst[index + 1] < lst[index - 1]:
                return False
    return True

print(check_non_decreasing([3, 4, 2, 3]))
