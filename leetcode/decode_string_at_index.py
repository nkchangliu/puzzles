def decode_string(s, k):
    index = 1
    s_index = 0
    lst = []
    while index <= k:
        c = s[s_index]
        s_index += 1
        if not c.isdigit():
            lst.append(c)
            index += 1
        else:
            index += (int(c) - 1) * (index - 1)
    if not s[s_index - 1].isdigit():
        return s[s_index - 1]
    else:
        old_index = index // int(s[s_index - 1])
        new_k = k % old_index
        return decode_string(s, new_k or old_index)
