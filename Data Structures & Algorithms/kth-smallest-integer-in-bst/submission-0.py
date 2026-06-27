# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def dfs(node):
            if not node:
                return None
            
            left = dfs(node.left)

            self.count += 1

            if self.count == k:
                return node.val
            else:
                right = dfs(node.right)
                return left or right

        return dfs(root)
                    