class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(r, c):
            if r >= m or c >= n:
                return float('inf')
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return memo[(r, c)]

        return dfs(0, 0)