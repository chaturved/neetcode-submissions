class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i, d2 in enumerate(reversed(num2)):
            d2_int = int(d2)
            for j, d1 in enumerate(reversed(num1)):
                d1_int = int(d1)
                val = d1_int * d2_int + res[i + j]
                res[i+j] = val % 10
                res[i+j+1] += val // 10
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return ''.join(map(str, reversed(res)))


