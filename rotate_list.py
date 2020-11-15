"""Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 
Try solving this without creating a copy of the list. How many swap or move operations do you need?"""


def rotate(a, n):
    for i in a[:n]:
        a.remove(i)
        a.append(i)

        
def rotate_list(a, n):
    a.extend(a[:n])
    return a[n:]

             
a = [1, 2, 3, 4, 5, 6]
rotate_list(a, 2)
