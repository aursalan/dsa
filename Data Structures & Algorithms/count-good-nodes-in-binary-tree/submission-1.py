# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:


        count = 0
        head = [root.val]

        def countNodes(root):
            nonlocal count

            if root == None:
                return
        
            if root.val >= head[-1]:
                count+=1      
                head.append(root.val)

            countNodes(root.left)
            countNodes(root.right)

            if root.val == head[-1]:
                head.pop()

            return

        countNodes(root)

        return count