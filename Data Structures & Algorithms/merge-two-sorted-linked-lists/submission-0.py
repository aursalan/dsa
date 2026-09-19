# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        merge = head

        while list1!=None or list2!=None:

            if list1 == None:
                merge.next = list2
                list2 = list2.next
                merge = merge.next
            
            elif list2 == None:
                merge.next = list1
                list1 = list1.next
                merge = merge.next

            elif list1.val < list2.val:
                merge.next = list1
                list1 = list1.next
                merge = merge.next
            
            else:
                merge.next = list2
                list2 = list2.next
                merge = merge.next
            
        head = head.next

        return head