class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros, right_ones = 0, 0
        for i in range(len(s) - 1, -1, -1):
            right_ones += 1 if s[i] == "1" else 0
        
        res = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                left_zeros += 1
            else:
                right_ones -= 1
            
            res = max(res, left_zeros + right_ones)
        
        return res
            



            
