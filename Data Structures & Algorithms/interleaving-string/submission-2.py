class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        k = i + j
        dfs(i, j) = 
        i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j) 
        or j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1)
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                k = i + j
                if i < m and s1[i] == s3[k] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < n and s2[j] == s3[k] and dp[i][j + 1]:
                    dp[i][j] =  True
        
        return dp[0][0]
                
