# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            
            l_height, l_diam = dfs(node.left)
            r_height, r_diam = dfs(node.right)

            height = 1 + max(l_height, r_height)
            diameter = max(l_diam, r_diam, l_height + r_height)

            return height, diameter
        
        _, diameter = dfs(root)
        return diameter
        
