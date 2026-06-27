# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            self.max_sum = max(self.max_sum, node.val + max(left, 0) + max(right, 0))

            return node.val + max(left, right, 0)
        
        _ = dfs(root)
        return self.max_sum
