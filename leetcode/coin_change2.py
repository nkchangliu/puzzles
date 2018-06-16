def coin_change(amount, coins):
    if not amount:
        return 1
    if not coins:
        return 0
    counts = [0] * (1 + amount)
    for i in range(amount + 1):
        if i % coins[0] == 0:
            counts[i] = 1

    for i in range(1, len(coins)):
        new_counts = [0] * (1 + amount)
        new_counts[0] = 1
        for j in range(amount + 1):
            new_counts[j] = counts[j]
            if j >= coins[i]:
                new_counts[j] += new_counts[j - coins[i]]

        counts = new_counts

    return counts[-1]

print(coin_change(5, [1, 2, 5]))
