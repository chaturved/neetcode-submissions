class Solution:
    def rob(self, nums: List[int]) -> int: 
        """
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr, prev = max(prev + nums[i], curr), curr
        
        return curr