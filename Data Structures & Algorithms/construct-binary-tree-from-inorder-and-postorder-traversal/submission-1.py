# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder will give left -> root -> right
        # postorder will give left -> right -> root
        inorder_map = {val: i for i, val in enumerate(inorder)}

        idx = len(postorder) - 1

        def dfs(l, r):
            nonlocal idx
            if l > r:
                return None

            root_val = postorder[idx]
            idx -= 1
            index = inorder_map[root_val]

            node = TreeNode(root_val)
            
            node.right = dfs(index + 1, r)
            node.left = dfs(l, index - 1)

            return node
        
        return dfs(0, len(postorder) - 1)

