"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'."""


def makepalindrome(s, k):
    d = list(s)
    for i in d:
        b = d[:]
        b.remove(i)
        w = ''.join(b)
        if w == w[::-1]:
            return w
            print(w, 'end')
        c = b[:]
        for j in c:
            c.remove(j)
            v = ''.join(c)
            if v == v[::-1]:
                return v
            c = b[:]
    else:
        print(f"can't make palindrom by removing at most 2 letters from {s}")

print(makepalindrome('waterrfetawx', 2))
