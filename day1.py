import itertools as it


""" Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""


def day1(A, k):
    ac = it.combinations(A,2)
    for i in ac:
        if sum(i) == k:
            return (True, i)
    else:
        return False


a = [10, 15, 3, 7]
print(day1(a, 17))
