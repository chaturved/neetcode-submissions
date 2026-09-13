class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        r = 0
        res, prev, curr = 0, 0, 0
        while r < len(nums):
            if nums[r] > prev:
                curr += nums[r]
                prev = nums[r]
                r += 1
            else:
                res = max(res, curr)
                curr, prev = 0, 0
                l = r
        
        return max(res, curr)

                

