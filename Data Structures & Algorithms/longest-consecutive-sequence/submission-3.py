class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        length, max_length = 0, 0
        i = 0
        while i < len(nums):
            if nums[i] - 1 not in set_nums:
                num = nums[i]
                while num in set_nums:
                    length += 1
                    num += 1
                max_length = max(max_length, length)
                length = 0
            i += 1
        
        return max_length
        