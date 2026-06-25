# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "#"
            return f"^{node.val},{serialize(node.left)},{serialize(node.right)}"
        
        def kmp(text, pattern):
            s = pattern + "$" + text
            lps = [0] * len(s)
            j = 0
            for i in range(1, len(s)):
                while j > 0 and s[i] != s[j]:
                    j = lps[j - 1]
                if s[i] == s[j]:
                    j += 1
                lps[i] = j
                if j == len(pattern):
                    return True
            return False
        
        return kmp(serialize(root), serialize(subRoot))
        