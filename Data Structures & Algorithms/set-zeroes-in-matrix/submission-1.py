class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [], []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row.append(r)
                    col.append(c)
        
        for r in row:
            for c in range(n):
                matrix[r][c] = 0
        
        for r in range(m):
            for c in col:
                matrix[r][c] = 0
                
        