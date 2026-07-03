class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        queue = deque()

        for r in [0, m - 1]:
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "T"
                    queue.append((r, c))
        
        for r in range(m):
            for c in [0, n - 1]:
                if board[r][c] == "O":
                    board[r][c] = "T"
                    queue.append((r, c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    queue.append((nr, nc))
        

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


