# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_value = float('-inf'), max_value = float('inf')):
            if not node:
                return True
            
            if not (min_value < node.val < max_value):
                return False
            
            left = dfs(node.left, min_value, node.val)
            right = dfs(node.right, node.val, max_value)

            return left and right
        
        return dfs(root)