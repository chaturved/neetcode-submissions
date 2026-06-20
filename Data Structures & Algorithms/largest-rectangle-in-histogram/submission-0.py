class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        
        for r in range(n):
            while stack and heights[stack[-1]] > heights[r]:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = r - left - 1
                max_area = max(max_area, height * width)
            stack.append(r)
        
        while stack:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = n - left - 1
            max_area = max(max_area, height * width)
        
        return max_area