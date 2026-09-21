# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None:
            return

        length = 0

        firstHead = head
        current = head


        while current!=None:
            length+=1
            current=current.next 


        swap = (length + 1) // 2

        current = head 
        count = 0


        while count<swap-1:
            current = current.next
            count+=1

        reverse = None
        lastHead = current
        current = current.next
        lastHead.next = None

        while current!=None:

            nextNode = current.next
            current.next = reverse
            reverse = current 
            current = nextNode 


        while reverse != None:
            leftNodes = firstHead.next
            rightNodes = reverse.next

            firstHead.next = reverse
            reverse.next = leftNodes

            firstHead = leftNodes
            reverse = rightNodes