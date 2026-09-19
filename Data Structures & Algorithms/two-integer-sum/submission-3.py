class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_index = {}
        for i, num in enumerate(nums):
            if target - num in complement_index:
                return [complement_index[target - num], i]
            
            complement_index[num] = i
        
        return None