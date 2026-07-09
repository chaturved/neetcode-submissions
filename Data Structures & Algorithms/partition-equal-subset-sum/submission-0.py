class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False
        target = summ // 2

        memo = {}
        def dfs(i, total):
            if total == target:
                return True
            if i == len(nums):
                return False
            if (i, total) in memo:
                return memo[(i, total)]

            res = False
            for j in range(i, len(nums)):
                if dfs(j + 1, total + nums[j]):
                    res = True
                    break

            memo[(i, total)] = res
            return res

        return dfs(0, 0)