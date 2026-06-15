class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i, num in enumerate(nums):
            if target - num in pair:
                return [pair[target - num], i]
            else:
                pair[num] = i
        
        return -1