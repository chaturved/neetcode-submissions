class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        blocked = [[0] * n for _ in range(n)]
        result = []
        directions = [
            (0, 1), (0, -1), 
            (1, 0), (-1, 0), 
            (-1, -1), (1, -1), 
            (1, 1), (-1, 1)
        ]

        def mark(r, c, val):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < n and 0 <= nc < n:
                    blocked[nr][nc] += val
                    nr += dr
                    nc += dc

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for c in range(n):
                if board[row][c] == "." and blocked[row][c] == 0:
                    board[row][c] = "Q"
                    mark(row, c, 1)
                    backtrack(row + 1)
                    mark(row, c, -1)
                    board[row][c] = "."
        
        backtrack(0)
        return result