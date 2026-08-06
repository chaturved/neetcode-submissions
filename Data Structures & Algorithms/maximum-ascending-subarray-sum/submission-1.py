class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        running_sum = 0
        prev = 0
        for num in nums:
            if prev >= num:
                running_sum = num
                prev = num
            else:
                running_sum += num
                prev = num
                result = max(result, running_sum)
        
        return result