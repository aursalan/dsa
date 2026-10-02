# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True
        
        def depth(root):
            nonlocal balanced

            if root == None:
                return 0
            
            left = depth(root.left)
            right = depth(root.right)

            if abs(left-right) >= 2:
                balanced = False
            
            return max(left, right) + 1

        depth(root)

        return balanced 

        