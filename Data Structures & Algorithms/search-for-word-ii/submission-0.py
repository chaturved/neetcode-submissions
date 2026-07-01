class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        trie = Trie()
        trie.add_words(words)

        result = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(node, char_lst, r, c):
            if node.end_of_word:
                result.append("".join(char_lst))
                node.end_of_word = False

            if r < 0 or c < 0 or r >= m or c >= n:
                return

            char = board[r][c]

            if char not in node.children:
                return

            board[r][c] = "#"

            for dr, dc in directions:
                char_lst.append(char)
                nr, nc = r + dr, c + dc
                dfs(node.children[char], char_lst, nr, nc)
                char_lst.pop()

            board[r][c] = char

        for r in range(m):
            for c in range(n):
                dfs(trie.root, [], r, c)

        return result


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.end_of_word = True

    def add_words(self, words):
        for word in words:
            self.add_word(word)