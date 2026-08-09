class Solution:
    def minOperations(self, s: str) -> int:
        def min_operations(bit):
            ops = 0
            for i, char in enumerate(s):
                if i % 2 == 0:
                    ops += (char != bit)
                else:
                    ops += (char == bit)
            
            return ops
        
        return min(min_operations('0'), min_operations('1'))
                