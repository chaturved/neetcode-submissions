class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        if i == 0:
            reverse(0, len(nums) - 1)
            return 

        pivot_index = i - 1
        
        next_min, next_min_index = float('inf'), -1
        while i < len(nums):
            if nums[pivot_index] < nums[i] < next_min:
                next_min, next_min_index = nums[i], i
            i += 1
        
        nums[pivot_index], nums[next_min_index] = nums[next_min_index], nums[pivot_index]
        
        reverse(pivot_index + 1, len(nums) - 1)


        
        

        