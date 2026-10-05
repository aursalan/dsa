from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):

        if root == None:
            return []

        queue = deque([root])
        res = [[root.val]]

        while queue:
            
            node = []
            val = []

            while queue:
                root = queue.popleft()
                
                if root.left:
                    node.append(root.left)
                    val.append(root.left.val)
                
                if root.right:
                    node.append(root.right)
                    val.append(root.right.val)

            queue = deque(node)
            
            if len(val) > 0: 
                res.append(val)
        
        return res