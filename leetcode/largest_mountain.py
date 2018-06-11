def longest_mountain(lst):
    ans, base = 0, 0
    while base < len(lst):
        end = base
        if end + 1 < len(lst) and lst[end] < lst[end + 1]:
            while end + 1 < len(lst) and lst[end] < lst[end + 1]:
                end += 1
            if end + 1 < len(lst) and lst[end] > lst[end + 1]:
                while end + 1 < len(lst) and lst[end] > lst[end + 1]:
                    end += 1
                ans = max(ans, end - base + 1)
        base = max(base+1, end)
    return ans

print(longest_mountain([2,1,4,7,3,2,5]))
