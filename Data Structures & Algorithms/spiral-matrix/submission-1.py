class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])
            
            if top == bottom or left == right:
                break
            
            for j in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][j])
            
            for i in range(bottom - 1, top, -1):
                result.append(matrix[i][left])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return result