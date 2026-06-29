class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(comb, total = 0, start = 0):
            if total > target:
                return

            if total == target:
                result.append(comb[:])
                return
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(comb, total + nums[i], i)
                comb.pop()
        
        backtrack([])
        return result
