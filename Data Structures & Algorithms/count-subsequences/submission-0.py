class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def count_subsequences(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
                
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if s[i] == t[j]:
                memo[(i, j)] = count_subsequences(i + 1, j + 1) + count_subsequences(i + 1, j)
                return memo[(i, j)]
            
            memo[(i, j)] = count_subsequences(i + 1, j)
            return memo[(i, j)]
        
        return count_subsequences(0, 0)
        