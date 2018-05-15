from fractions import gcd

def rotate(nums, k):
    l = len(nums)
    g = gcd(k,l)
    m = l//g
    for i in range(g):
        for j in range(m):
            nxt = (i+k*(j+1)) % l
            nums[nxt], nums[i] = nums[i], nums[nxt]
    return nums

print(rotate([1, 2, 3, 4, 5, 6, 7], 2))
