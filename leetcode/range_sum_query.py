class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.sums = []
        total = 0
        for x in nums:
            total += x
            self.sums.append(total)

    def update(self, i, val):
        for ind in range(i, len(self.nums)):
            self.sums[ind] += (val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]
