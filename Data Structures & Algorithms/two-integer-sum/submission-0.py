class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            pair_value = target - nums[i]
            if pair_value in indices:
                return [indices[pair_value], i]
            indices[nums[i]] = i
        
        return [0, 0]