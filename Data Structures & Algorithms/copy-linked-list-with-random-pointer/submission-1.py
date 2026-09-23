"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None:
            return None
        
        copies = {}

        current = head

        while current:
            copies[current] = Node(current.val)
            current = current.next

        
        current = head

        while current:
            copies[current].next = copies.get(current.next)
            copies[current].random = copies.get(current.random)
            current = current.next
        
        return copies[head]