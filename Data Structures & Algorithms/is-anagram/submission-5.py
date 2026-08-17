class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0] * 26
        freq_t = [0] * 26

        for char in s:
            freq_s[ord(char) - ord('a')] += 1
        
        for char in t:
            freq_t[ord(char) - ord('a')] += 1
        
        return freq_s == freq_t