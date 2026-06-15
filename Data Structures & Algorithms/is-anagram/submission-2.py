class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            s_freq[index] += 1
        
        t_freq = [0] * 26
        for char in t:
            index = ord(char) - ord('a')
            t_freq[index] += 1
        
        return s_freq == t_freq
            
        
