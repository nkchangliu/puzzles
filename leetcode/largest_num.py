
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y + x

def largestNumber(self, nums):
    largest_num = ''.join(sorted(map(str, nums), key=LargeNumKey)
    return '0' if largest_num[0] == '0' else largest_num

