class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def lookForIsland(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            if grid[i][j] == "1" and (i, j) not in visited:
                visited.add((i, j))
                lookForIsland(i - 1, j)
                lookForIsland(i + 1, j)
                lookForIsland(i, j - 1)
                lookForIsland(i, j + 1)
        
        lands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    lands.add((i, j))
                    
        visited = set()
        islands_count = 0
        for (i, j) in lands:
            if (i, j) not in visited:
                lookForIsland(i, j)
                islands_count += 1
        
        return islands_count
        
                    


        
        