class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        def update(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or grid[i][j] == -1:
                return
            
            visited.add((i, j))
            queue.append((i, j))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                grid[i][j] = dist
                update(i, j + 1)
                update(i, j - 1)
                update(i - 1, j)
                update(i + 1, j)
            dist += 1

        

        