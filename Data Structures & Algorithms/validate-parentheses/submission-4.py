class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        vaild_par = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in vaild_par:
                stack.append(char)
            elif not stack or char != vaild_par[stack.pop()]:
                    return False
        
        return not stack