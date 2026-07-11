import sys
sys.setrecursionlimit(20000)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = {}
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]

            max_length = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    max_length = max(max_length, dfs(nr, nc))

            memo[(r, c)] = 1 + max_length
            return memo[(r, c)]
        
        max_length = 0
        for r in range(m):
            for c in range(n):
                max_length = max(max_length, dfs(r, c))
        
        return max_length
        

            
