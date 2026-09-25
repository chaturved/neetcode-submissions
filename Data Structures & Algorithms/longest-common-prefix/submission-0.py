class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            trie.insert(word)

        return trie.lcp()


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.is_end = True

    def lcp(self):
        curr = self.root
        chars = []

        while len(curr.children) == 1 and not curr.is_end:
            key = next(iter(curr.children))
            chars.append(key)
            curr = curr.children[key]

        return "".join(chars)