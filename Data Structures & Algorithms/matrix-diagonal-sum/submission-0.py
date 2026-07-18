class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diagonal_sum = 0

        for i in range(n):
            diagonal_sum += mat[i][i]
        
        for i in range(n):
            if i == n - 1 - i:
                continue
            diagonal_sum += mat[i][n - 1 - i]
        
        return diagonal_sum
        