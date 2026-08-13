class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0

        for r in range(k):
            total += arr[r]
        
        result = 0
        if total / k >= threshold:
            result += 1

        l, r = 0, k - 1
        while r < len(arr):
            total -= arr[l]

            l += 1
            r += 1

            if r >= len(arr):
                break
            
            total += arr[r]

            if total / k >= threshold:
                result += 1
        
        return result
            

