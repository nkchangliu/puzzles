def coin_change(coins, amount):
    coins = sorted(coins)
    counts = [amount + 1] * (amount + 1)
    counts[0] = 0

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if i >= coins[j]:
                counts[i] = min(counts[i], counts[i - coins[j]] + 1)
    return counts[-1] if counts[-1] <= amount else -1

print(coin_change([1, 2, 5], 11))
