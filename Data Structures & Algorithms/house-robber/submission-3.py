class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            if i < 0:
                return 0

            rob_curr = nums[i] + dfs(i - 2)
            not_rob_curr = dfs(i - 1)

            memo[i] = max(rob_curr, not_rob_curr)
            return memo[i]
        
        return dfs(len(nums) - 1)