class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        node = root
        offset = 0

        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            offset += node.val
            node.val = offset
            node = node.left

        return root