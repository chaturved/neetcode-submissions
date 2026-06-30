class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []
        cols = set()
        diag = set()
        anti_diag = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for c in range(n):
                if c in cols or (row - c) in diag or (row + c) in anti_diag:
                    continue
                
                board[row][c] = "Q"
                cols.add(c)
                diag.add(row - c)
                anti_diag.add(row + c)

                backtrack(row + 1)

                board[row][c] = "."
                cols.remove(c)
                diag.remove(row - c)
                anti_diag.remove(row + c)
        
        backtrack(0)
        return result