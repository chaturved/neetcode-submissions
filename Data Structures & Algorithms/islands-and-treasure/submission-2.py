class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(r, c, count):
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            
            if grid[r][c] < count:
                return
            
            grid[r][c] = count

            for dr, dc in directions:
                dfs(r + dr, c + dc, count + 1)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(r, c, 0)

