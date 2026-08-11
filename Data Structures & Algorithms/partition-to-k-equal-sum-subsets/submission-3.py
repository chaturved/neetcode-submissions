class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        used = [False] * len(nums)

        def dfs(start, curr, remaining_k):
            if remaining_k == 0:
                return True
            
            if curr == target:
                return dfs(0, 0, remaining_k - 1)
            
            for i in range(start, len(nums)):
                if used[i]:
                    continue

                if curr + nums[i] > target:
                    continue
                
                used[i] = True
                if dfs(i + 1, curr + nums[i], remaining_k):
                    return True
                used[i] = False
            
            return False
        
        return dfs(0, 0, k)