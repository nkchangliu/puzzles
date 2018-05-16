# find the nth largest number which prime factors are only 2, 3, 5

def find_num(n):
    lst = [1]
    i, j, k = 0, 0, 0
    while len(lst) < n:
        if lst[i]*2 == lst[j]*3 == lst[k]*5:
            lst.append(lst[i]*2)
            i += 1
            j += 1
            k += 1
        elif lst[i]*2 == lst[j]*3 and lst[j]*3 < lst[k]*5:
            lst.append(lst[i] * 2)
            i += 1
            j += 1
        elif lst[i]*2 == lst[k]*5 and lst[i]*2 < lst[j]*3:
            lst.append(lst[i] * 2)
            i += 1
            k += 1
        elif lst[j]*3 == lst[k]*5 and lst[j]*3 < lst[i]*2:
            lst.append(lst[j]*3)
            j += 1
            k += 1
        elif lst[i]*2 < lst[j]*3 and lst[i]*2 <lst[k]*5:
            lst.append(lst[i]*2)
            i += 1
        elif lst[j]*3 < lst[i]*2 and lst[j]*3 < lst[k]*5:
            lst.append(lst[j]*3)
            j += 1
        else:
            lst.append(lst[k]*5)
            k += 1

    return lst[-1]


