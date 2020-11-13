"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}."""


def smallest_interval(s):
    start = min(s, key=lambda s: s[0])
    end = max(s, key=lambda s: s[1])
    return {start[1], end[0]}


print(smallest_interval([[0,3], [2, 6], [3, 4], [6, 9]]))
