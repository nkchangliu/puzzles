def majority(lst):
    if len(lst) <= 1:
        return lst
    count1, count2 = 0, 0
    candidate1, candidate2 = 0, 0
    for num in lst:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    count1, count2 = 0, 0
    for num in lst:
        if num == candidate1:
            count1 += 1
        if num == candidate2:
            count2 += 1
    res = []

    if count1 > len(lst) // 3:
        res.append(candidate1)
    if count2 > len(lst) // 3:
        res.append(candidate2)

    return res

print(majority([1,2,1,1,1,3,3,4,3,3,3,4,4,4]))

