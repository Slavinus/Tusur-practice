def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    c1 = [0] * 26
    c2 = [0] * 26
    for ch in s1:
        c1[ord(ch) - ord('a')] += 1
    for ch in s2:
        c2[ord(ch) - ord('a')] += 1
    return c1 == c2