class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        amount[i] = max(amount[i - 2] + cost[i], amount[i - 1])
        """

        def house_robber(nums):
            prev = nums[0]
            curr = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                curr, prev = max(prev + nums[i], curr), curr

            return curr

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        return max(house_robber(nums[:n - 1]), house_robber(nums[1:]))