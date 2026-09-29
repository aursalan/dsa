# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):

        if root == None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        if root and root.left and root.right:
            
            root.left, root.right = root.right, root.left
            return root
        
        elif root and root.left:
            root.right = root.left
            root.left = None
        
        elif root and root.right:
            root.left = root.right
            root.right = None

        return root