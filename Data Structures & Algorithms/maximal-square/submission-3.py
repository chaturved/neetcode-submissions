class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= m or j >= n or matrix[i][j] == "0":
                return 0
            
            memo[(i, j)] = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            return memo[(i, j)]
        
        max_size = 0
        for i in range(m):
            for j in range(n):
                max_size = max(max_size, dfs(i, j))
        
        return max_size * max_size