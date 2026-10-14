class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for bought in range(0, 2):
                dp[i][bought] = max(
                    dp[i + 1][bought], 
                    prices[i] + dp[i + 1][0] if bought else -prices[i] + dp[i + 1][1]
                )
        
        return dp[0][0]

