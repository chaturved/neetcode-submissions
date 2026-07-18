class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False

        for c in range(n):
            if matrix[0][c] == 0:
                first_row_zero = True

        for r in range(m):
            if matrix[r][0] == 0:
                first_col_zero = True

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0