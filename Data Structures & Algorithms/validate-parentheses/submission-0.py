class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack:
                return False
            elif char != brackets[stack.pop()]:
                return False
        
        return True if not stack else False
