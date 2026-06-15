class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        output[i] = (nums[0] * ... nums[i - 1]) * (nums[len(nums) - 1] * ... nums[i + 1])

        [5, 2, 4, 6]
        left_product = [1, 5, ]
        """

        left_product = [1] * len(nums)
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        
        right_product = [1] * len(nums)
        for j in range(len(nums) - 2, -1, -1):
            right_product[j] = right_product[j + 1] * nums[j + 1]
        
        output = []
        for left, right in zip(left_product, right_product):
            output.append(left * right)
        
        return output
        
