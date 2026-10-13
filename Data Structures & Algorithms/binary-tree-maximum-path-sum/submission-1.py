# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = float("-inf")

        def dfs(root):
            nonlocal maxSum

            if root == None: return 0

            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))

            maxSum = max(maxSum, left+right+root.val)

            return max(left+root.val, right+root.val)

        dfs(root)
        return maxSum