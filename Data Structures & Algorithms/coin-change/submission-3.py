class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m, n = len(coins), amount
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][amount] = 0

        for i in range(m - 1, -1, -1):
            for total in range(n - 1, -1, -1):
                take = 1 + dp[i][total + coins[i]] if total + coins[i] <= amount else float('inf')
                skip = dp[i + 1][total]
                dp[i][total] = min(take, skip)
        
        res = dp[0][0]

        if res == float('inf'):
            return -1
        
        return res
        
