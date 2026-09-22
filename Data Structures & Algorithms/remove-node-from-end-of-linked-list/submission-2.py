# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        head, length = self.reverseLinkedList(head)

        previousNode = None
        currentNode = head
        currentLength = 1

        while currentNode!=None:
            if n == 1 and length == 1:
                head = None
                break
            
            elif n==1 and length > 1:
                head = currentNode.next
                break
            
            elif n == length and currentLength == n:
                previousNode.next = None
                break

            elif n == currentLength:
                previousNode.next = currentNode.next
                break
            
            previousNode = currentNode
            currentNode = currentNode.next
            currentLength+=1
        
        return self.reverseLinkedList(head)[0]

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        reverseNode = None
        length = 0

        while head!=None:

            nextNode = head.next
            head.next = reverseNode
            reverseNode = head
            head = nextNode
            length+=1

        return reverseNode, length




                

            
        