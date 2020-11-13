"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4"""


def anagram_index(w, s):
    a = [''.join(i) for i in it.permutations(w, len(w))]
    start = 0
    indexes = []
    #for i in range(len(s)):
    for j in a:
        for i in range(len(s)):
            v = s.find(j, start)
            if v == -1:
                break
            indexes.append(v)
            start = v + len(w)
        start = 0
    return indexes


print(anagram_index('ab', 'abxaba'))
