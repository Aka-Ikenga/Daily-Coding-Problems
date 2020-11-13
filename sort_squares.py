"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81]."""

a = [-9, -2, 7, 8, 9]


def square_sorted(int_list):

    int_list_square = [i**2 for i in int_list]
    int_list_square.sort()
    return int_list_square


print(square_sorted(a))


