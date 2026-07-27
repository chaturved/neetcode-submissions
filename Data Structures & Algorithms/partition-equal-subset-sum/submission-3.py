class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        since all the elements must be part of either of the subset
        and there sums are equal, the question translates to find a subset of nums with the sum / 2

        a + b = n
        a = b = x
        2x = n
        x = n / 2

        here since all nums are integer, n needs to even to find a subset

        find subset is either taking curr element or skipping at i index
        we can keep a running_sum
        """

        nums_sum, length = sum(nums), len(nums)

        if nums_sum % 2 == 1:
            return False
        
        target = nums_sum // 2

        memo = {}

        def dfs(i, running_sum):
            if (i, running_sum) in memo:
                return memo[(i, running_sum)]

            if running_sum == target:
                return True
            
            if i >= length:
                return False
            
            memo[(i, running_sum)] = dfs(i + 1, running_sum) or dfs(i + 1, nums[i] + running_sum)
            return memo[(i, running_sum)]
        
        return dfs(0, 0)

        

