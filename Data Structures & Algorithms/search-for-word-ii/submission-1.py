class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                node = node.children.setdefault(char, TrieNode())
            node.word = word

        result = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(node, r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return

            char = board[r][c]
            if char not in node.children:
                return

            node = node.children[char]
            if node.word:
                result.append(node.word)
                node.word = None 

            board[r][c] = "#"
            for dr, dc in directions:
                dfs(node, r + dr, c + dc)
            board[r][c] = char

        for r in range(m):
            for c in range(n):
                dfs(root, r, c)

        return result


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None