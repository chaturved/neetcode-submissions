class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        length = len(s)

        def is_palindrome(i, j):
            return s[i:j+1] == s[i:j+1][::-1]

        def backtrack(part, i):
            if i == length:
                result.append(part[:])
                return
            
            for j in range(i, length):
                if is_palindrome(i, j):
                    part.append(s[i:j+1])
                    backtrack(part, j + 1)
                    part.pop()
        
        backtrack([], 0)
        return result
        