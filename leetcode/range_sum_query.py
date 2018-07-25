class NumArray:

    def __init__(self, nums):
        self.size = len(nums)
        self.segement = self.build_tree(nums)

    def build_tree(self, nums):
        segement = [0] * (2 * len(nums) - 1)
        for i in range(len(nums)):
            segement[i + len(nums) - 1] = nums[i]
        for i in range(len(nums) - 2, -1, -1):
            segement[i] = segement[2 * i + 2] + segement[2 * i + 1]
        return segement

    def update(self, i, val):
        ind = (i + self.size - 1)
        self.segement[ind] = val
        while ind > 0:
            if ind % 2 == 0:
                right = ind
                left = ind - 1
            else:
                right = ind + 1
                left = ind
            self.segement[(ind - 1) // 2] = self.segement[left] + self.segement[right]
            ind = (ind - 1) // 2


    def sumRange(self, i, j):
        l = i + self.size - 1
        r = j + self.size - 1
        sum = 0
        while (l <= r):
            if (l%2) == 0:
                sum += self.segement[l]
                l += 1
            if (r%2) == 1:
                sum += self.segement[r]
                r -= 1
            l = (l - 1) // 2
            r = (r - 1) // 2
        return sum


lst = [1, 2, 3, 4, 5]
nums = NumArray(lst)
print(nums.segement)
nums.update(2, 10)
print(nums.segement)
print(nums.sumRange(2, 4))
