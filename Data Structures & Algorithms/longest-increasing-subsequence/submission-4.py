class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev_index):
            if i == len(nums):
                return 0
            
            if (i, prev_index) in memo:
                return memo[(i, prev_index)]
            
            prev_num = float('-inf') if prev_index == -1 else nums[prev_index]

            take = 1 + dfs(i + 1, i) if nums[i] > prev_num else 0
            skip = dfs(i + 1, prev_index)

            memo[(i, prev_index)] = max(take, skip)
            return memo[(i, prev_index)]
        
        return dfs(0, -1)
            

