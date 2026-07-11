class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if (r, c) in memo:
                return memo[(r, c)]

            best = float('inf')
            if r + 1 < m:
                best = min(best, dfs(r + 1, c))
            if c + 1 < n:
                best = min(best, dfs(r, c + 1))

            memo[(r, c)] = grid[r][c] + best
            return memo[(r, c)]

        return dfs(0, 0)