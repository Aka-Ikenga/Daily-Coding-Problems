"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""


class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)
    
    def __str__(self):
        return str(self.data)
    

class LinkedList:
    
    def __init__(self, num):
        self.head = None
        self.num = num
        self.l = []
        self.growlist()
    
    def __repr__(self):
        rep = '->'.join(self.l)
        return rep

    def growlist(self):
        n = str(self.num)
        for i in n[::-1]:
            node = Node(int(i))
            node.next = self.head
            self.head = node
            self.l.append(str(self.head))
    
    def printlist(self):
        cnode = self.head
        while cnode:
            print(cnode)
            cnode = cnode.next
    
    def __add__(self, other):
        ans = self.num + other.num
        return LinkedList(ans)
        
        
A = LinkedList(25)   
B = LinkedList(99)
A + B
