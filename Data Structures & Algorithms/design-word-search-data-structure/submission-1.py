class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        length = len(word)

        def dfs(node, i):
            if i == length:
                return node.end_of_word

            char = word[i]
            if char == ".":
                return any(dfs(child, i + 1) for child in node.children.values())

            if char in node.children:
                return dfs(node.children[char], i + 1)

            return False

        return dfs(self.root, 0)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False