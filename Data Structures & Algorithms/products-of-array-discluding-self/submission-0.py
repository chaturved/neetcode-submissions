class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [2, 4, 6, 10]
        [1, 1 * 2, 1 * 2 * 4, 1 * 2 * 4 * 6]
        [1 * 10 * 6 * 4, 1 * 10 * 6, 1 * 10, 1]
        """
        left_product = [1]
        for i in range(1, len(nums)):
            left_product.append(left_product[i - 1] * nums[i - 1])
        
        right_product = [1]
        for i in range(1, len(nums)):
            right_product.append(right_product[i - 1] * nums[-i])
        
        result = []
        for l, r in zip(left_product, right_product[::-1]):
            result.append(l * r)
        
        return result