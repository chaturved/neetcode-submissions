class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        """
        1 2 3
        4 5 6
        7 8 9

        1 4 7
        2 5 8
        3 6 9
        """

        for r in range(n):
            for c in range(n):
                if r < c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in matrix:
            l, r = 0, n - 1
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1
        




