from collections import deque 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = []
        node = {}

        if len(lists) == 0:
            return None

        for i in lists:
            
            if i and i.val in node:

                node[i.val].append(i)
            
            elif i:
                node[i.val] = deque([i])
            

        while node:

            minVal = min(node)
            minNode = node[minVal].popleft()

            if len(node[minVal]) == 0:
                del node[minVal]

            nextNode = minNode.next

            if nextNode and nextNode.val in node:
                node[nextNode.val].append(nextNode)
            
            elif nextNode:
                node[nextNode.val] = deque([nextNode])
            
            if len(res) == 0:
                res.append(minNode)
                res[-1].next = None
            
            else:
                res[-1].next = minNode
                res.append(minNode) 

        return res[0] if len(res)!=0 else None