class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n] = 0
        dp[m][n - 1] = 0
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]