class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        res = 0
        carry = 0
        i = 0
        while i < 32:
            bit1 = (a >> i) & 1
            bit2 = (b >> i) & 1
            d = bit1 ^ bit2 ^ carry
            carry = (bit1 & bit2) | (bit1 & carry) | (bit2 & carry)
            res |= (d << i)
            i += 1
        return res if res <= 0x7FFFFFFF else ~(res ^ mask)