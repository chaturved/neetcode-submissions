class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                is_palindrome[i][j] = s[i] == s[j] and (j - i <= 2 or is_palindrome[i + 1][j - 1])
                count += 1 if is_palindrome[i][j] else 0
        
        return count