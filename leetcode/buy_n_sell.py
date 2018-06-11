def buy_sell(nums):
    if not nums:
        return 0
    min_price, max_profit = nums[0], 0
    for num in nums:
        if num < min_price:
            min_price = num
        if num - min_price > max_profit:
            max_profit = num - min_price

    return max_profit

