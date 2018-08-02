from collections import Counter

def find_anagram(lst, s):
    s_table = Counter(s)
    m_table = Counter(lst[0: len(s)])
    res = []
    for i in range(len(lst) - len(s)):
        if m_table == s_table:
            res.append(i)
        m_table[lst[i]] -= 1
        if m_table[lst[i]] == 0:
            del m_table[lst[i]]
        if lst[i + len(s)] not in m_table:
            m_table[lst[i + len(s)]] = 1
        else:
            m_table[lst[i + len(s)]] += 1
    if s_table == m_table:
        res.append(i + 1)
    return res

print(find_anagram("cbaebabacd", "abc"))
