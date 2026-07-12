class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        the sum of nums[i...j] = prefix[j] - prefix[i - 1]
        = sum(nums[0..j]) - prefix[i - 1]
        to maximize  the sum of nums[i...j] we have for a fixed sum(nums[0..j])
        we have to minimze prefix[i - 1]
        """

        running_sum = 0
        min_prefix = 0
        max_sum = float('-inf')
        for num in nums:
            running_sum += num
            max_sum = max(max_sum, running_sum - min_prefix)
            min_prefix = min(min_prefix, running_sum)
        
        return max_sum

        