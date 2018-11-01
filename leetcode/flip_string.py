'''
We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.
'''




def count_flips(s):
    end_zero = 0
    smallest_flip = 0
    for i in range(len(s)):
        num = s[i]
        new_end_zero = end_zero if num == '0' else end_zero + 1
        new_end_one = smallest_flip if num == '1' else smallest_flip + 1
        smallest_flip = min(new_end_zero, new_end_one)
        end_zero = new_end_zero
    return smallest_flip

print(count_flips("100000001010000"))


