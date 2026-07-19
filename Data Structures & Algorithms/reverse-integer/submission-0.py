class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(abs(x))
        x_str_rev = x_str[::-1]
        x_int_rev = int(x_str_rev)
        x_int_rev *= -1 if x < 0 else 1
        
        if -2 ** 31 <= x_int_rev <= 2 ** 31 - 1:
            return x_int_rev
        
        return 0