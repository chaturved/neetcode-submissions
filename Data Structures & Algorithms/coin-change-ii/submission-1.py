class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return 0
            
            if total == amount:
                return 1

            if (i, total) in memo:
                return memo[(i, total)]
            
            combinations = dfs(i, total + coins[i]) + dfs(i + 1, total)
            memo[(i, total)] = combinations
            return combinations
        
        return dfs(0, 0)
            
            
