# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        either p and q are connected with parent then parent is the LCA
        or p and q are connected which means node at top between the two is the LCA
        """

        def dfs(node):
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            return left or right
        
        return dfs(root)
            
