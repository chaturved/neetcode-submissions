class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        [inf, -1, 0, inf]
        [inf, inf, inf, -1]
        [inf, -1, inf, -1, inf]
        [0, -1, inf, inf]
        """

        """
        [3, -1, 0, 1]
        [2, 2, 1, -1]
        [1, -1, 2, -1]
        [0, -1, 3, 4]
        """

        def dfs(i, j, cnt = 0):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == -1 or grid[i][j] < cnt:
                return

            grid[i][j] = cnt
            
            dfs(i, j + 1, cnt + 1)
            dfs(i, j - 1, cnt + 1)
            dfs(i + 1, j, cnt + 1)
            dfs(i - 1, j, cnt + 1)
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    dfs(i, j)
        
        