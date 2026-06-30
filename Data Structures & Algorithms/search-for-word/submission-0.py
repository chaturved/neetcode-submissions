class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        visited = set()

        def backtrack(r, c, i):
            if i == w:
                return True

            if r < 0 or r == m or c < 0 or c == n:
                return False
            
            if (r, c) in visited:
                return False
            
            if board[r][c] != word[i]:
                return False

            visited.add((r, c))

            found = (
                backtrack(r, c + 1, i + 1) or 
                backtrack(r, c - 1, i + 1) or
                backtrack(r + 1, c, i + 1) or 
                backtrack(r - 1, c, i + 1)
            )

            visited.remove((r, c))

            return found
        
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
        
        return False