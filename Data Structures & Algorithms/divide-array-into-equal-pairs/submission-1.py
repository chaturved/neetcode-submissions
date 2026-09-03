class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for value in freq.values():
            if value % 2:
                return False
        
        return True