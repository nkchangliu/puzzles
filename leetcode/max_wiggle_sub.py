def max_wiggle_sub(lst):
    if len(lst) < 2:
        return len(lst)
    wiggle_dict = {}
    wiggle_dict[0] = (1, None, lst[0])

    for i in range(1, len(lst)):
        last_length, last_diff, last_num = wiggle_dict[i - 1]
        curr_diff = lst[i] - last_num
        if (not last_diff and curr_diff) or (curr_diff < 0 and last_diff > 0) or (curr_diff > 0 and last_diff < 0):
            wiggle_dict[i] = (last_length + 1, curr_diff, lst[i])
        else:
            wiggle_dict[i] = (last_length, last_diff, lst[i])
    max_length, _, _ = wiggle_dict[len(lst) - 1]

    return wiggle_dict

print([33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15])
print(max_wiggle_sub([33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]))
