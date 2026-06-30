class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            queue = deque([(r, c)])
            board[r][c] = "T"
            while queue:
                r, c = queue.popleft()
                for dr, dc in deltas:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                        board[nr][nc] = "T"
                        queue.append((nr, nc))

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == "O":
                    bfs(i, j)
        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == "O":
                    bfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"