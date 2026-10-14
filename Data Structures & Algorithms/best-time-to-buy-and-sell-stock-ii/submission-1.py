class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, bought):
            if (i, bought) in memo:
                return memo[(i, bought)]

            if i >= len(prices):
                return 0
            
            skip = dfs(i + 1, bought)
            include = 0
            if bought:
                include = prices[i] + dfs(i + 1, False)
            else:
                include = -prices[i] + dfs(i + 1, True)

            memo[(i, bought)] = max(skip, include)
            return memo[(i, bought)]
        
        return dfs(0, False)
