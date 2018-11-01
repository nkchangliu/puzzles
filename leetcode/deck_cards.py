from collections import Counter
from math  import gcd
from functools import reduce

def deck_cards(lst):
    if not lst:
        return False
    counts = Counter(lst)
    return  reduce(gcd, counts.values()) >= 2
l =[]
print(deck_cards(l))

# does not work could be 4 == 2
# make sure that there gcd
