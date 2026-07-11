class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def is_increasing():
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            
            return True
        
        def is_decreasing():
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
            
            return True
        
        return is_increasing() or is_decreasing()