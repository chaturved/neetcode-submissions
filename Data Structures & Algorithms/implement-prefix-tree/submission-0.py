class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children
            if char not in curr:
                curr[char] = TreeNode(char)
            curr = curr[char]
            
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            curr = curr.children
            if char not in curr:
                return False
            curr = curr[char]

        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            curr = curr.children
            if char not in curr:
                return False
            curr = curr[char]

        return True

class TreeNode:
    def __init__(self, val: str = ""):
        self.val = val
        self.children = {}
        self.end_of_word = False
        
        