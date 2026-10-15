# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        preorder = []

        def dfs(root):

            if root == None:
                preorder.append("#")
                return
            
            preorder.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

            return
        
        dfs(root)

        return ",".join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        values = iter(data.split(","))

        def dfs():
            val = next(values)

            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
