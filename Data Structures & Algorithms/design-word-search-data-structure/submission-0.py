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
        # curr = self.root
        # for char in word:
        #     if char not in curr.children:
        #         return False
        #     curr = curr.children[char]
        
        # return curr.end_of_word

        length = len(word)

        def dfs(node, i):
            if i == length:
                return node.end_of_word
            
            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            
            if word[i] == ".":
                return any(dfs(children_node, i + 1) for children_node in node.children.values())

            return False
        
        return dfs(self.root, 0)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
