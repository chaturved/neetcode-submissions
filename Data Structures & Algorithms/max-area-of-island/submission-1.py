class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs():
            total = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        total += 1
                        queue.append((nr, nc))
            return total
        
        max_area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    queue.append((r, c))
                    max_area = max(max_area, bfs())
        
        return max_area


