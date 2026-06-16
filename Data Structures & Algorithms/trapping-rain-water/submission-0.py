class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        current_max = 0
        for curr_height in height:
            current_max = max(current_max, curr_height)
            max_left.append(current_max)
        
        max_right = [0] * len(height)
        current_max = 0
        for i in range(len(height) - 1, -1, -1):
            current_max = max(current_max, height[i])
            max_right[i] = current_max
        
        total_area = 0
        for i in range(len(height)):
            total_area += min(max_left[i], max_right[i]) - height[i]
        
        return total_area