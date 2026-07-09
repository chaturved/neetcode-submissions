class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = { len(nums): 0 }
        def dfs(l):
            if l in memo:
                return memo[l]

            largest = nums[l - 1] if l > 0 else float('-inf')

            max_longest = 0
            for i in range(l, len(nums)):
                if nums[i] > largest:
                    max_longest = max(max_longest, 1 + dfs(i + 1))
            
            memo[l] = max_longest
            return max_longest
        
        return dfs(0)