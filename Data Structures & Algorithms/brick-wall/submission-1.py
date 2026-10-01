class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        freq = defaultdict(int)
        for row in wall:
            total = 0
            for width in row[:-1]:
                total += width
                freq[total] += 1

        best = max(freq.values(), default=0)
        return len(wall) - best