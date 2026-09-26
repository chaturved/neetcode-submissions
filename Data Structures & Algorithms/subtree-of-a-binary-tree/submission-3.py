# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subTree(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
            
            return subTree(node1.left, node2.left) and subTree(node1.right, node2.right)

        def search(node):
            if not node:
                return False
            
            if node.val == subRoot.val:
                if subTree(node, subRoot):
                    return True

            return search(node.left) or search(node.right)
        
        return search(root)
        



        