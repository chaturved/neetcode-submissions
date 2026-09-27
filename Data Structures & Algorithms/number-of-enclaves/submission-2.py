class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()

        for r in [0, m - 1]:
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 2
        
        for r in range(m):
            for c in [0, n - 1]:
                if grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 2
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    grid[nr][nc] = 2
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    count += 1
        
        return count

        




