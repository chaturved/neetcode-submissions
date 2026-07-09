class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        dp = {len(s): True}

        def parition(l):
            if l in dp:
                return dp[l]

            node = root
            for i in range(l, len(s)):
                char = s[i]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_end and parition(i + 1):
                    dp[l] = True
                    return True

            dp[l] = False
            return False

        return parition(0)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False