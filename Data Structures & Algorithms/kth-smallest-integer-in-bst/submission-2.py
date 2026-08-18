class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        result = 0
        def dfs(node):
            nonlocal cnt, result
            if not node:
                return 

            dfs(node.left)
            cnt += 1

            if cnt == k:
                result = node.val
                return

            dfs(node.right)
        
        dfs(root)
        return result