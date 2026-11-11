class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, subset = [], []
        nums.sort()
        def backtrack(i):
            res.append(subset[:])

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])
                backtrack(j + 1)
                subset.pop()
        
        backtrack(0)
        return res
                
            