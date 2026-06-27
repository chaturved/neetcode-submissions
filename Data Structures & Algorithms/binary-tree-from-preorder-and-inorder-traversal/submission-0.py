# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            node = TreeNode(preorder[0])
            left_size = inorder.index(preorder[0])

            node.left = dfs(preorder[1:left_size + 1], inorder[:left_size])
            node.right = dfs(preorder[left_size + 1:], inorder[left_size + 1:])

            return node
        
        return dfs(preorder, inorder)