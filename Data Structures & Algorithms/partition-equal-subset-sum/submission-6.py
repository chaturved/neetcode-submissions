class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        memo = {}
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if total == 0:
                return True
            
            if i >= len(nums):
                return False

            memo[(i, total)] = dfs(i + 1, total - nums[i]) or dfs(i + 1, total)
            return memo[(i, total)]
        
        return dfs(0, total // 2)