class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        x = 1...limit
        remaining, n - x
        y = 1...min(limit, n-x)
        z = 1...n-x-y
        """
        res = 0
        for x in range(0, limit + 1):
            rem = n - x
            y_low, y_high = max(0, rem - limit), min(limit, rem)
            res += max(0, y_high - y_low + 1)
        
        return res

