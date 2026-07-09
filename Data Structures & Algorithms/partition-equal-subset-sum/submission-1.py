class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False
        target = summ // 2
        n = len(nums)

        memo = {}
        def dfs(i, total):
            if total == target:
                return True
            if i == n or total > target:
                return False
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i + 1, total) or dfs(i + 1, total + nums[i])
            return memo[(i, total)]

        return dfs(0, 0)