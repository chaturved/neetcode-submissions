class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_index = defaultdict(int)
        for i in range(len(nums)):
            nums_index[nums[i]] = i

        current = min(nums)
        max_value = max(nums)
        max_cnt = 0
        cnt = 0

        while current <= max_value:
            if current in nums_index:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
            current += 1
            
        return max(max_cnt, cnt)
                

            