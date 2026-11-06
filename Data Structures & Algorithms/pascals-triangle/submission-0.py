class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        """

        pascal = [[1 for _ in range(i + 1)] for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        
        return pascal
