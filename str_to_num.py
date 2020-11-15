"""Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers: "a""x 1""a -2"
"""


def strtonum(s):
    try:
        value = float(s)
        return f'{s} is a valid literal for string to number conversion'
    except ValueError:
        return f'{s} is an invalid literal for string to number conversion'


strtonum('-90.8-e5')
