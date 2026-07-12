class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                for k in range(l, r + 1):
                    left = nums[l - 1] if l - 1 >= 0 else 1
                    right = nums[r + 1] if r + 1 < n else 1
                    left_dp = dp[l][k - 1] if k - 1 >= l else 0
                    right_dp = dp[k + 1][r] if k + 1 <= r else 0
                    dp[l][r] = max(dp[l][r], left * nums[k] * right + left_dp + right_dp)

        return dp[0][n - 1]