class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)
    
        visited = set()
        longest = 0
        for num in exists:
            if num in visited:
                continue
            
            current = num
            while current in exists:
                visited.add(current)
                current += 1

            longest = max(longest, current - num)
        
        return longest


