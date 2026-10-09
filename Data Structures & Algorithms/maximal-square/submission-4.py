class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= m or j >= n:
                return 0
            
            down = dfs(i + 1, j)
            right = dfs(i, j + 1)
            diag =  dfs(i + 1, j + 1)
            
            memo[(i, j)] = 1 + min(down, right, diag) if matrix[i][j] == "1" else 0
            return memo[(i, j)]
        
        dfs(0, 0)
        
        return max(memo.values(), default=0) ** 2