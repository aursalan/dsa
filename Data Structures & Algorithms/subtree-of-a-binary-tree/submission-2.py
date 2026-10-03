# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def isSubtree(self, root, subRoot):

        def compare(root, subRoot):

            if root == None and subRoot == None:
                return True
            
            if root and subRoot == None:
                return False
            
            if root == None and subRoot:
                return False
            
            if root and subRoot and root.val != subRoot.val:
                return False
            
            return compare(root.left, subRoot.left) and compare(root.right, subRoot.right)
        
        if root == None:
            return False
        
        if root.val == subRoot.val:
            if compare(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)