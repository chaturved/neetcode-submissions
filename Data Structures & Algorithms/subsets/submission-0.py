class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(subset, start_index = 0):
            result.append(subset[:])
            for i in range(start_index, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        

        backtrack([])
        return result