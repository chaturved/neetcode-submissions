class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        curr_max = curr_min = nums[0]
        result = nums[0]

        for i in range(1, n):
            curr_max, curr_min = max(nums[i], curr_max * nums[i], curr_min * nums[i]), min(nums[i], curr_max * nums[i], curr_min * nums[i])
            result = max(result, curr_max)
        
        return result