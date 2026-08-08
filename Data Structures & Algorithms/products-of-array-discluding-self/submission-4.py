class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        product[i] = product[0...i-1] * product[i+1..] = left_product[i] * right_product[i]
        """

        left_product = [1] * len(nums)
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        
        right_product = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        
        return [left * right for left, right in zip(left_product, right_product)]
