"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false."""

def shift_string(a, b):
    for i in range(1, len(a)):
        s = a[:i]
        c = a.replace(s, '')
        for j in range(1, len(c)+1):
            t = list(c)
            t.insert(j, s)
            if ''.join(t) == b: return True
    
    else: return False

print(shift_string('abc', 'acb'))
