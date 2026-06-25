# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [None]
            
            traversal = [node.val]

            left = dfs(node.left)
            traversal.extend(left)

            right = dfs(node.right)
            traversal.extend(right)

            return traversal
        
        tree_traversal = dfs(root)
        subtree_traversal = dfs(subRoot)
        return any(tree_traversal[i : i + len(subtree_traversal)] == subtree_traversal for i in range(len(tree_traversal) - len(subtree_traversal) + 1))


