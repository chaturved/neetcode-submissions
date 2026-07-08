class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        is_palindrome = [[False for _ in range(n)] for _ in range(n)]
        best_i, best_len = 0, 1

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                is_palindrome[i][j] = (s[i] == s[j]) and (j - i <= 2 or is_palindrome[i + 1][j - 1])
                if is_palindrome[i][j] and best_len < j - i + 1:
                    best_i = i
                    best_len = j - i + 1
        
        return s[best_i : best_i + best_len]