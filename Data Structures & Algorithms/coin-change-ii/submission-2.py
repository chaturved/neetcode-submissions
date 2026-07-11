class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, a):
            if i >= len(coins) or a < 0:
                return 0
            
            if a == 0:
                return 1

            if (i, a) in memo:
                return memo[(i, a)]
            
            combinations = dfs(i, a - coins[i]) + dfs(i + 1, a)
            memo[(i, a)] = combinations
            return combinations
        
        return dfs(0, amount)
            
            
