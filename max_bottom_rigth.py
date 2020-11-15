"""## Day 122
Good morning! Here's your coding interview problem for today.

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins."""


def bottom_right(n): 
    c = n.shape[1] - 1
    r = n.shape[0] - 1
    right_down = np.sum(n[0]) + np.sum(n[:, c]) - n[0, c]
    down_right = np.sum(n[:, 0]) + np.sum(n[r]) - n[r, 0]
    return max(right_down, down_right)


n = np.array([0, 3, 1, 1, 2, 0, 0, 4, 1, 5, 3, 1]).reshape(3,4)
bottom_right(n)
