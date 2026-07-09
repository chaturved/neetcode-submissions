class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(l, prev):
            if l == len(nums):
                return 0
            
            if (l, prev) in memo:
                return memo[(l, prev)]

            skip = dfs(l + 1, prev)
            
            include = 0
            if prev == -1 or nums[l] > nums[prev]:
                include = 1 + dfs(l + 1, l)
            
            memo[(l, prev)] = max(skip, include)
            return memo[(l, prev)]
        
        return dfs(0, -1)