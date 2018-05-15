# list of numbers with each number representing max jump check if can reach the end

def can_jump(nums):
    if len(nums) <= 1:
        return True
    elif nums[0] == 0:
        return False
    for i in range(1, nums[0] + 1):
        if can_jump(nums[i:]):
            return True
    return False


def can_jump_dp(nums):
    can_jump = {}
    can_jump[len(nums) - 1] = True
    for ind in reversed(range(len(nums) - 1)):
        can_jump[ind] = False
        for i in range(1, nums[ind] + 1):
            if can_jump[i + ind]:
                can_jump[ind] = True
                break
    return can_jumpi[0]


def can_jump_one_pass(nums):
    if len(nums) <= 1:
        return True
    can_jump = len(nums) - 1
    for ind in reversed(range(len(nums) - 1)):
        if ind + nums[ind] >= can_jump:
            can_jump = ind
    return can_jump == 0


print(can_jump_one_pass([2, 3, 1, 1, 4]))
print(can_jump_one_pass([3, 2, 1, 0, 4]))
print(can_jump_one_pass([2, 0]))
