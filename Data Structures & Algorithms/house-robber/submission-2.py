class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        define amount[i] is max amount that can be made at ith house
        two possibilites: it can be either robbing ith and not robbing

        if robbing ith house then we can only take the money made till i - 2
        as i - 1 cannot be robbed in this case: amount[i - 2] + cost[i]
        else amount[i - 1]
        take the max of these 

        amount[i] = max(amount[i - 2] + cost[i], amount[i - 1])
        """

        n = len(nums)

        if n == 1:
            return nums[0]

        prev = nums[0]
        curr = max(prev, nums[1])

        for i in range(2, n):
            curr, prev = max(prev + nums[i], curr), curr
        
        return curr
