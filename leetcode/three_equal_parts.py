'''
Given an array A of 0s and 1s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.
start time: 6:36
end time: 7:10
'''

'''
[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]

divide it into three parts
one brute force way is to
for i in range 0 to end
    for j in range i + 1 to end
        check the three parts and see if the same

if three parts represents the same number means they should have the same amount of 1s, but not necessarily the same 0s (bc of leading 0s)
count the number of 1s-- there are 3 if cant divide by 3--> return false
means each part will have one 1 exactly
now let's look at the first number
get the pattern between the first one and the last one in the first number
check if the pattern between the first and last 1 the same

first have a dictionary of the appearance of 1 and it's index
then find out the start and end for those three components
compare the string pattern in between
also need to check trailing zeros, we can get the index based on the last part of number

O(n) runtime

'''

def divide_array(arr):
    one_index = {}
    count = 0
    for i, num in enumerate(arr):
        if num:
            count += 1
            one_index[count] = i
    if count % 3 != 0:
        return [-1, -1]
    if not count:
        return [0, 2]
    num_one_each = count // 3
    trailing_zeros = len(arr) - 1 - one_index[3*num_one_each]
    first_s, first_e = one_index[1], one_index[num_one_each]
    second_s, second_e  = one_index[1+num_one_each], one_index[2* num_one_each]
    third_s, third_e = one_index[1+2*num_one_each], one_index[3*num_one_each]
    # check count of trailing zeros
    if second_s - first_e > trailing_zeros and third_s - second_e > trailing_zeros and \
            check_same(arr, first_s, first_e, second_s, second_e) and check_same(arr, first_s, first_e, third_s, third_e):
                return [one_index[num_one_each]+trailing_zeros, one_index[2* num_one_each]+1+trailing_zeros]
    return [-1, -1]

def check_same(arr, first_s, first_e, second_s, second_e):
    if first_e - first_s != second_e - second_s:
        return False
    for i in range(first_e - first_s +1):
        if arr[first_s + i] != arr[second_s + i]:
            return False
    return True


