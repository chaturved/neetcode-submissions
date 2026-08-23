# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            
            rob_left, not_rob_left = dfs(node.left)
            rob_right, not_rob_right = dfs(node.right)

            rob_this = node.val + not_rob_left + not_rob_right
            not_rob_this = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)

            return rob_this, not_rob_this
        
        return max(dfs(root))
            
        
            