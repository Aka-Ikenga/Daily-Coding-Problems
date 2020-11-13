""" Day 113
This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
Follow-up: given a mutable string representation, can you perform this operation in-place?
"""

def reverse_string(s):
    ss = s.split(' ')
    w = ss[::-1]
    w = ' '.join(w)
    s = ' '.join(s.split(' ')[::-1])
    return w, s

print(reverse_string('hello world here'))
