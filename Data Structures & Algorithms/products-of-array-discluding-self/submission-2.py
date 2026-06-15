class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        
        right_product = 1
        for j in range(len(nums) - 2, -1, -1):
            right_product *= nums[j + 1]
            output[j] *= right_product
        
        return output