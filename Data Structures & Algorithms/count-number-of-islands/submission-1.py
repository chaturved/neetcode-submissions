class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            
            if grid[r][c] != "1":
                return
            
            grid[r][c] = "0"
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count
            
