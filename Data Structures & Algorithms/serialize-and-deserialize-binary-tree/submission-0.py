# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ["N"]
            
            lst = [str(node.val)]

            left = dfs(node.left)
            lst.extend(left)

            right = dfs(node.right)
            lst.extend(right)

            return lst

        preorder = dfs(root)
        return " ".join(preorder)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(" ")
        self.i = 0
        def dfs():
            if preorder[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(preorder[self.i]))
            self.i += 1

            left = dfs()
            right = dfs()

            node.left = left
            node.right = right

            return node
        
        return dfs()


        

        
        