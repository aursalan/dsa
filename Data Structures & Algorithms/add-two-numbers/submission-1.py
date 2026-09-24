# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        currentL1 = l1
        numL1 = []

        while currentL1:
            numL1.append(currentL1.val)
            currentL1 = currentL1.next

        numL1 = "".join(str(num) for num in numL1[::-1])

        currentL2 = l2
        numL2 = []

        while currentL2:
            numL2.append(currentL2.val)
            currentL2 = currentL2.next

        numL2 = "".join(str(num) for num in numL2[::-1])

        print(numL1, numL2)


        value = int(numL1) + int(numL2)

        print(value)

        res = ListNode()
        head = res

        while value!=0:

            res.val = value % 10
            value = value // 10
            if value != 0:
                res.next = ListNode()
                res = res.next


        return head





    