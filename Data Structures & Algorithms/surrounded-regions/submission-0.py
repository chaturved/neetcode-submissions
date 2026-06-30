class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m = len(board)
        n = len(board[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    zeros.append((i, j))
        
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        for i, j in zeros:
            if (i, j) in visited:
                continue
            
            queue = deque([(i, j)])
            visited.add((i, j))
            region = [(i, j)]
            touches_border = (i == 0 or i == m - 1 or j == 0 or j == n - 1)

            while queue:
                r, c = queue.popleft()

                for dr, dc in deltas:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        region.append((nr, nc))
                        if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                            touches_border = True
            
            if not touches_border:
                for r, c in region:
                    board[r][c] = "X"