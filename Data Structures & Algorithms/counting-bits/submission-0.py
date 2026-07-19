class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n + 1):
            j = i
            count = 0
            while j:
                count += j & 1
                j >>= 1
            result.append(count)
        
        return result
            
                