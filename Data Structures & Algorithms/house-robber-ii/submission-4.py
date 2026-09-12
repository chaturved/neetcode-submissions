class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(l, r):
            n = r - l
            if n == 0:
                return 0
            if n == 1:
                return nums[l]

            prev = nums[l]
            curr = max(nums[l], nums[l + 1])

            for i in range(2, n):
                curr, prev = max(curr, prev + nums[l + i]), curr
                
            return curr

        if len(nums) == 1:
            return nums[0]

        return max(helper(0, len(nums) - 1), helper(1, len(nums)))