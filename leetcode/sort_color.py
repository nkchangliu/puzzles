# sort by color in one pass

# use three pointers, one at the front monitoring which is the last place of 0's,
# one montoring which is the place to put in 2's
# one iterate over the lst

def sort_color(lst):
    if len(lst) < 2:
        return lst
    zero, curr = 0, 0
    two = len(lst) - 1
    while zero < len(lst) and lst[zero] == 0:
        zero += 1
    curr = zero
    while two >= 0 and lst[two] == 2:
        two -= 1

    while curr <= two:
        print(lst)
        print(zero)
        print(curr)
        print(two)
        if lst[curr] == 2:
            lst[curr], lst[two] = lst[two], lst[curr]
            two -= 1
            while two >= 0 and lst[two] == 2:
                two -= 1
        if lst[curr] == 0 and curr >= zero:
            lst[curr], lst[zero] = lst[zero], lst[curr]
            zero += 1
            while zero < len(lst) and lst[zero] == 0:
                zero += 1

        curr += 1
    return lst

print(sort_color([2,0,2,1,1,0]))
