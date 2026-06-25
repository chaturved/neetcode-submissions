# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [None]

            left = dfs(node.left)
            right = dfs(node.right)

            return [node.val] + left + right
        
        return dfs(p) == dfs(q)