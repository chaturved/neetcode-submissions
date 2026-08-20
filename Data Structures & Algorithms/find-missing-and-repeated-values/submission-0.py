class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = (n ** 2 * (n ** 2 + 1)) // 2
        freq = defaultdict(int)
        for i in range(n):
            for j in range(n):
                total -= grid[i][j]
                freq[grid[i][j]] += 1
        
        """
        total + a - b = 0 => total = b - a
        """

        a = 0
        for key, value in freq.items():
            if value == 2:
                a = key
                break
        
        return [a, total + a]
        
