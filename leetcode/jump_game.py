# return the minimum number of jumps needed to get to the end

def jump_game(nums):
    jumps = [0] * len(nums)
    for ind in reversed(range(len(nums) - 1)):
        jumps[ind] = 1 + find_minimum(nums, ind, jumps)
    return jumps

def find_minimum(nums, ind, jumps):
    mini = float("infinity")
    for i in range(1, nums[ind] + 1):
        if ind + i < len(nums) and jumps[i + ind] < mini:
            mini = jumps[i + ind]
    return mini


print(jump_game([2, 3, 0, 1, 4]))
