def letter_combination(code):
    c_dict = {}
    c_dict[2] = set(['a','b', 'c'])
    c_dict[3] = set(['d', 'e', 'f'])
    c_dict[4] = set(['g', 'h', 'i'])
    c_dict[5] = set(['j', 'k', 'l'])
    c_dict[6] = set(['m', 'n', 'o'])
    c_dict[7] = set(['p', 'q', 'r', 's'])
    c_dict[8] = set(['t','u', 'v'])
    c_dict[9] = set(['w', 'x', 'y', 'z'])

    curr = set([""])
    for num in code:
        new_curr = set()
        chars = c_dict[int(num)]
        for sub_s in curr:
            for c in chars:
                new_s = sub_s + c
                new_curr.add(new_s)
        curr = new_curr
    return curr

print(letter_combination('23'))
