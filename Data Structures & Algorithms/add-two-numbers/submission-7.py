# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        currentL1 = l1
        currentL2 = l2

        result = ListNode()
        head = result
        
        carry = 0

        while currentL1 or currentL2:

            value = carry

            if currentL1:
                value += currentL1.val

            if currentL2:
                value += currentL2.val

            result.val = value % 10
            carry = value // 10 

            currentL1 = currentL1.next if currentL1 else None
            currentL2 = currentL2.next if currentL2 else None

            if currentL1 or currentL2:
                result.next = ListNode() 
                result = result.next
            
        if carry:
            result.next = ListNode(carry)
        
        return head
    
