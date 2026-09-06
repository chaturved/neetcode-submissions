# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        lst_str = []
        def dfs(node):
            if not node:
                lst_str.append("N")
                return
            
            lst_str.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return " ".join(lst_str)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        lst_str = data.split(" ")
        i = 0
        def dfs():
            nonlocal i
            if i >= len(lst_str) or lst_str[i] == "N":
                i += 1
                return None

            new_node = TreeNode(int(lst_str[i]))
            i += 1
            
            new_node.left = dfs()
            new_node.right = dfs()

            return new_node
        
        return dfs()

