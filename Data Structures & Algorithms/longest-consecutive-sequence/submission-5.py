class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)

        longest = 0
        for num in exists:
            if num - 1 in exists:
                continue
            
            current = num
            while current in exists:
                current += 1

            longest = max(longest, current - num)
        
        return longest