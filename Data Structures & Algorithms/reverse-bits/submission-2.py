class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32:
            d = n & 1
            res = res | d << (31 - i)
            n = n >> 1
            i += 1
        
        return res
        
