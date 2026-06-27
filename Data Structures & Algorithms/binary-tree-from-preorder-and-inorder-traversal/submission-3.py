# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(in_start, in_end):
            if in_start > in_end:
                return None
            
            node = TreeNode(preorder[self.pre_idx])
            left_size = inorder_map[preorder[self.pre_idx]]
            self.pre_idx += 1

            node.left = dfs(in_start, left_size - 1)
            node.right = dfs(left_size + 1, in_end)

            return node
        
        return dfs(0, len(inorder) - 1)