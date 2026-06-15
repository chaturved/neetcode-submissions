class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            if heights[i] <= heights[j]:
                max_area = max(max_area, heights[i] * (j - i))
                i += 1
            else:
                max_area = max(max_area, heights[j] * (j - i))
                j -= 1
        
        return max_area