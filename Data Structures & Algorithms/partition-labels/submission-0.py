class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_last_index = {}
        for i, char in enumerate(s):
            char_last_index[char] = i
        
        i = 0
        res = []
        while i < len(s):
            j = i
            count = 0
            while i <= j:
                j = max(j, char_last_index[s[i]])
                i += 1
                count += 1
            
            res.append(count)
        
        return res
            
            


