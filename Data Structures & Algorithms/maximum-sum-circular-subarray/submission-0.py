class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix, max_prefix = 0, 0
        best_min, best_max = float('inf'), float('-inf')
        for num in nums:
            prefix += num
            best_min = min(best_min, prefix - max_prefix)
            best_max = max(best_max, prefix - min_prefix)
            max_prefix = max(max_prefix, prefix)
            min_prefix = min(min_prefix, prefix)
        
        if best_max < 0:
            return best_max
            
        return max(best_max, prefix - best_min)