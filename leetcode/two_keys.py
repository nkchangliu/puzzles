'''
A AA 
AAA AAAA
AAAA AAAAA AAAAAA
'''
from queue import Queue

def two_keys(num):
    if num == 1:
        return 0
    q = Queue()
    q.put((2,1,2))

    while q:
        last_num, last_paste, last_move = q.get()
        print(last_num, last_paste, last_move)
        if last_num == num:
            return last_move
        q.put((last_num + last_paste, last_paste, last_move + 1))
        q.put((last_num + last_num, last_num, last_move + 2))
    return -1

def two_keys_prime(n):
    if n <= 1:
        return 0
    p = 2
    ans = 0
    while n > 1:
        while n % p == 0:
            n = n // p
            ans += p
        p += 1
    return ans


