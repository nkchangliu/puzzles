# group words that are anagrams together

def group_anagram(lst):
    word_dict = {}
    for word in lst:
        key = ''.join(sorted(word))
        if key not in word_dict:
            word_dict[key] = []
        word_dict[key].append(word)
    return list(word_dict.values())

print(group_anagram(["eat", "ate","tea","cow","jae"]))
