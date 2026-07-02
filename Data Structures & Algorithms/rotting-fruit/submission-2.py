class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        t = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            t += 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        
        if t == 0:
            return 0
        
        return t - 1
