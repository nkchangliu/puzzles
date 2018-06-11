import collections

def hand(hands, w):
    count = collections.Counter(hands)
    while count:
        start = min(count)
        for num in range(start, w + start):
            if num not in count:
                return False
            elif count[num] == 1:
                del count[num]
            else:
                count[num] -= 1
    return True

