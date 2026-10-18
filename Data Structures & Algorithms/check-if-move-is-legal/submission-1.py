class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, dr, dc):
            count = 0
            while 0 <= r < m and 0 <= c < n and board[r][c] != "." and board[r][c] != color:
                r += dr
                c += dc
                count += 1

            return count > 0 and 0 <= r < m and 0 <= c < n and board[r][c] == color

        return (
            dfs(rMove, cMove + 1, 0, 1) or
            dfs(rMove, cMove - 1, 0, -1) or
            dfs(rMove + 1, cMove, 1, 0) or
            dfs(rMove - 1, cMove, -1, 0) or
            dfs(rMove + 1, cMove + 1, 1, 1) or
            dfs(rMove - 1, cMove - 1, -1, -1) or
            dfs(rMove - 1, cMove + 1, -1, 1) or
            dfs(rMove + 1, cMove - 1, 1, -1)
        )