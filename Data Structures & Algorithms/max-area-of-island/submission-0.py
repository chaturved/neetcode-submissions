class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
        
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area
        

        for r in range(m):
            for c in range(n):
                max_area = max(max_area, dfs(r, c))
        
        return max_area


