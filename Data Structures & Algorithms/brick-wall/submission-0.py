class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        freq = defaultdict(int)
        for i in range(len(wall)):
            running_sum = 0
            for j in range(len(wall[i]) - 1):
                running_sum += wall[i][j]
                freq[running_sum] += 1
        
        return len(wall) - max(freq.values(), default = 0)
                