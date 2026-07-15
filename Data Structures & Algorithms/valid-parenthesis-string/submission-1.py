class Solution:
    def checkValidString(self, s: str) -> bool:
        left_par = []
        star = []
        for i, char in enumerate(s):
            if char == "(":
                left_par.append(i)
            elif char == "*":
                star.append(i)
            elif left_par:
                left_par.pop()
            elif star:
                star.pop()
            else:
                return False
        
        while left_par and star:
            if left_par.pop() > star.pop():
                return False
        
        return not left_par
        

