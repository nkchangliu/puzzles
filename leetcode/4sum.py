def four_sum(a, b, c, d):
    ab_dict, cd_dict = {}, {}

    for num1 in a:
        for num2 in b:
            ab_dict[num1 + num2] = 1 if num1 + num2 not in ab_dict else ab_dict[num1 + num2] + 1
    for num1 in c:
        for num2 in d:
            cd_dict[num1 + num2] = 1 if num1 + num2 not in cd_dict else cd_dict[num1 + num2] + 1

    count = 0
    for num in ab_dict:
        if -num in cd_dict:
            count += ab_dict[num] * cd_dict[-num]
    return count

print(four_sum([1, 2], [-2, -1], [-1, 2], [0, 2]))
