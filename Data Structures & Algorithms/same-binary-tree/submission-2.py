# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        sameTree = True

        def compare(p,q):

            nonlocal sameTree

            if p==None and q==None:
                return None,None
            
            if p and q == None:
                sameTree = False
                return p, None
            
            if q and p == None:
                sameTree = False
                return None, q 
        
            if p and q and p.val != q.val:
                sameTree = False
        
            return compare(p.left,q.left), compare(p.right,q.right)

        compare(p,q)

        return sameTree

        