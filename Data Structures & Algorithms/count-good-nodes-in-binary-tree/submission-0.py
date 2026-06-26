# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, current_max = float('-inf')):
            if not node:
                return 0
            
            count = 1 if node.val >= current_max else 0
            new_max = max(current_max, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count
        
        return dfs(root)

            
