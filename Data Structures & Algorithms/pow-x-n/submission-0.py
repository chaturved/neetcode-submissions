class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for _ in range(abs(n)):
            res *= x
        
        if n < 0:
            return 1 / res
        return res