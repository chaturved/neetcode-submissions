class Solution:
    def checkValidString(self, s: str) -> bool:
        left_par_min = 0
        left_par_max = 0
        for char in s:
            if char == "(":
                left_par_min += 1
                left_par_max += 1
            elif char == "*":
                left_par_min -= 1
                left_par_max += 1
            else:
                left_par_min -= 1
                left_par_max -= 1
            
            if left_par_max < 0:
                return False
            if left_par_min < 0:
                left_par_min = 0
        
        return left_par_min == 0
                    

        

