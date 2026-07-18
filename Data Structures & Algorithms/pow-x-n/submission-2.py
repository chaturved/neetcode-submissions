class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        N = abs(n)
        res, base = 1, x
        while N > 0:
            if N % 2 == 1:
                res *= base
            base *= base
            N //= 2
        
        return res if n >= 0 else 1 / res
