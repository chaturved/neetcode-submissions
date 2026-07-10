class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        min_prefix = 0
        max_sum = float('-inf')
        running_sum = 0
        for i in range(n):
            running_sum += nums[i]
            max_sum = max(max_sum, running_sum - min_prefix)
            min_prefix = min(min_prefix, running_sum)
        
        return max_sum