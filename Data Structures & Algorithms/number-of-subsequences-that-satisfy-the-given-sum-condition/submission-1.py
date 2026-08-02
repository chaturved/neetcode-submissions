class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        l, r = 0, len(nums) - 1
        total_count = 0

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                total_count += 2 ** (r - l)
                l += 1

        return total_count % (10 ** 9 + 7)