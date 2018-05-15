from collections import Counter

def most_common_word(paragraph, banned):
    words = paragraph.lower().split(" ")
    word_clean = [''.join([char for char in word if char.isalpha()]) for word in words]
    words_count = Counter(word_clean)
    banned_set = set(banned)

    sorted_words = reversed(sorted(words_count, key = lambda x: words_count[x]))
    for word in sorted_words:
        if word not in banned_set:
            return word



print(most_common_word("Mr Jae is a big monkey, donkey, monkey donkey monkey head", ["monkey"]))
