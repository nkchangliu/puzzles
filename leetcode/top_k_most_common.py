import collections

def top_k_words(lst, k):
    counts = collections.Counter(lst)
    sort_counts = sorted(counts, key = lambda word: (-counts[word], word))
    return sort_counts[0 : k]


