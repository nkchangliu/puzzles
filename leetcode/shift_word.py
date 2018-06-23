def shift(s, nums):
    count = 0
    for i in range(len(nums) - 1, -1, -1):
        count += nums[i]
        nums[i] = count

    new_s = ""
    for i in range(len(s)):
        new_char = chr((ord(s[i]) - ord('a') + nums[i])%26 + ord('a'))
        new_s += new_char
    return new_s

print(shift("abc", [3, 5, 9]))

