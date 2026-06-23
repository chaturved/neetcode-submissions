class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            if num in exists:
                return num
            exists.add(num)
        
        return -1