class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            
            curr = num
            length = 0
            while curr in nums_set:
                curr += 1
                length += 1
            
            max_length = max(max_length, length)
        
        return max_length
        

