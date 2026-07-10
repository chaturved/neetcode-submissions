class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        paths[r][c] = paths[r - 1][c] + paths[r][c - 1]
        paths[0][c] = 1
        paths[r][0] = 1
        """
        paths = [[0] * n for _ in range(m)]
        paths[0][0] = 1

        for r in range(1, m):
            paths[r][0] = 1
        
        for c in range(1, n):
            paths[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                paths[r][c] = paths[r - 1][c] + paths[r][c - 1]
        
        return paths[m-1][n-1]