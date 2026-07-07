class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        define amount[i] is max amount that can be made at ith house
        two possibilites: it can be either robbing ith and not robbing

        robbing ith means amount[i] = robbing amount[i - 2] + cost[i]
        skipping means just amount[i - 1]

        amount[i] = max(amount[i - 2] + cost[i], amount[i - 1])
        """

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        amount = [0] * n
        amount[0] = nums[0]
        amount[1] = max(amount[0], nums[1])

        for i in range(2, n):
            amount[i] = max(amount[i - 2] + nums[i], amount[i - 1])
        
        return amount[n - 1]

