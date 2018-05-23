def get_hint(secret, guess):
    cache = {}
    a, b = 0, 0
    for counter, value in enumerate(secret):
        if guess[counter] == value:
            a += 1
        else:
            cache[value] = cache[value] + 1 if value in cache else 1

    for counter, value in enumerate(guess):
        if value != secret[counter] and value in cache and cache[value] > 0:
            cache[value] -= 1
            b += 1

    return "{}A{}B".format(a, b)

print(get_hint("1123","0111"))
