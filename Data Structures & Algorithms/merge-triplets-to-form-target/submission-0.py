class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        mx, my, mz = 0, 0, 0
        for (a, b, c) in triplets:
            if a <= x and b <= y and c <= z:
                mx, my, mz = max(mx, a), max(my, b), max(mz, c)
                if mx == x and my == y and mz == z:
                    return True
        
        return False
                
        

        


