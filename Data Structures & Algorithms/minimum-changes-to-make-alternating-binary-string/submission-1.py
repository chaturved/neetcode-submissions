class Solution:
    def minOperations(self, s: str) -> int:
        def get_ops(char_even, char_odd):
            ops = 0
            for i, char in enumerate(s):
                if i % 2 == 0:
                    ops += 1 if char == char_odd else 0
                else:
                    ops += 1 if char == char_even else 0
            return ops
        
        return min(get_ops('0', '1'), get_ops('1', '0'))