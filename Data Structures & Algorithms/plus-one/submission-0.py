class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digit, carry = total % 10, 1 if total >= 10 else 0
            result.append(digit)
        
        if carry != 0:
            result.append(carry)

        return result[::-1]