# check if a list of strings follows the same pattern

def word_pattern(pattern, lst):
    pattern = list(pattern)
    lst = lst.split(" ")
    print(pattern)
    print(lst)
    if len(pattern) != len(lst):
        return False
    pattern_dict = {}
    lst_dict = {}
    for i in range(len(pattern)):
        if pattern[i] not in pattern_dict:
            pattern_dict[pattern[i]] = set()
        pattern_dict[pattern[i]].add(lst[i])
        if lst[i] not in lst_dict:
            lst_dict[lst[i]] = set()
        lst_dict[lst[i]].add(pattern[i])

    max_pattern =  len(pattern_dict[max(pattern_dict, key = lambda key: len(pattern_dict[key]))])
    max_lst =  len(lst_dict[max(lst_dict, key = lambda key: len(lst_dict[key]))])
    return max(max_pattern, max_lst) == 1
print(word_pattern("abba", "dog cat cat dog"))
