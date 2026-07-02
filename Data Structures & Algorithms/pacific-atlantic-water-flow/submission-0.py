class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        def pacific_bfs():
            queue = deque()
            visited = set()
            for r in range(m):
                queue.append((r, 0))
                visited.add((r, 0))
            
            for c in range(n):
                queue.append((0, c))
                visited.add((0, c))
            
            bfs(queue, visited)
            return visited
        
        def atlantic_bfs():
            queue = deque()
            visited = set()
            for r in range(m):
                queue.append((r, n - 1))
                visited.add((r, n - 1))
            
            for c in range(n):
                queue.append((m - 1, c))
                visited.add((m - 1, c))
            
            bfs(queue, visited)
            return visited
        
        pacific = pacific_bfs()
        atlantic = atlantic_bfs()

        common = pacific.intersection(atlantic)
        return [list(p) for p in common]