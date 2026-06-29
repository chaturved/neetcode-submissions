class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(comb, start = 0):
            comb_sum = sum(comb)
            if comb_sum > target:
                return

            if comb_sum == target:
                result.append(comb[:])
                return
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(comb, i)
                comb.pop()
        
        backtrack([])
        return result
