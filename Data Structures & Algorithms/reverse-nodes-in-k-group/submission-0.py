# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        
        current = head
        res = None

        while current:

            previousHead = head
            head = current
            count = 0
            previousNode = None
            nextNode = None

            while current and count!=k:      

                nextNode = current.next
                current.next = previousNode
                previousNode = current
                current = nextNode
                count+=1

            if count == k:

                head.next = current

                if previousHead != head:
                    previousHead.next = previousNode 

                else:
                    res = previousNode

            else:

                current = previousNode
                previousNode = None

                while current:
                    nextNode = current.next
                    current.next = previousNode
                    previousNode = current
                    current = nextNode
                
                previousHead.next = previousNode

        return res