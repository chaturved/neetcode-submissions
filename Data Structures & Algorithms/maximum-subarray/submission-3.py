class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, in_subarray):
            if i == len(nums) - 1:
                return nums[i]
            
            if (i, in_subarray) in memo:
                return memo[(i, in_subarray)]

            if in_subarray:
                result = max(nums[i], nums[i] + dfs(i + 1, True))
            else:
                result = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True) if i + 1 <= len(nums) - 1 else nums[i], nums[i])

            memo[(i, in_subarray)] = result
            return result
        
        return dfs(0, False)