# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_map = {}
        self.preorder = preorder
        self.inorder = inorder

        for i, value in enumerate(self.inorder):
            self.inorder_map[value] = i

        def dfs(pre_start, in_start, in_end):
            if in_start > in_end:
                return None
            
            node = TreeNode(preorder[pre_start])
            left_size = self.inorder_map[preorder[pre_start]]

            node.left = dfs(pre_start + 1, in_start, left_size - 1)
            node.right = dfs(pre_start + left_size - in_start + 1, left_size + 1, in_end)

            return node
        
        return  dfs(0, 0, len(inorder) - 1)