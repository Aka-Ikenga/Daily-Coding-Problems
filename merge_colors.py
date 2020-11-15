"""This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |"""


def merge_colors(c):
    return list(set(c)^{'R', 'G', 'B'})[0]

def return_pair(a):
    if len(set(a)) == 1:
        return a[:1], 0
    
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            return a[i:i+2], i  # return the new pair to merge and there position

def cc(a):
    b, i = return_pair(a)
    if len(b) == 1:
        return b[0]
    
    d = merge_colors(b)
    a.pop(i)
    a.pop(i)
    a.insert(0, d)
    print(d, a)
    return cc(a)

a = ['R', 'G', 'B', 'G', 'B']
cc(a)
