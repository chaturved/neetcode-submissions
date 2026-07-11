class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[i][a] = (dp[i][a - coins[i]] if a - coins[i] >= 0 else 0) + dp[i + 1][a]
                
        return dp[0][amount]
