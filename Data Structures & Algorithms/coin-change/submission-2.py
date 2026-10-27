class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if total == amount:
                return 0

            if i == n or total > amount:
                return float("inf")

            take = 1 + dfs(i, total + coins[i])
            skip = dfs(i + 1, total)

            memo[(i, total)] = min(take, skip)
            return memo[(i, total)]

        res = dfs(0, 0)

        if res == float("inf"):
            return -1
        
        return res