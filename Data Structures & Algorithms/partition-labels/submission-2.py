class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i
        
        result = []
        l = 0
        while l < len(s):
            substring_length = 0
            r = l
            while l <= r:
                r = max(r, last_index[s[l]])
                l += 1
                substring_length += 1
            result.append(substring_length)
        
        return result
            
            
            



