class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        s1_freq = [0] * 26
        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1
        
        s2_freq = [0] * 26
        for i in range(len(s1)):
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        l, r = 0, len(s1) - 1
        while r < len(s2):
            if s1_freq == s2_freq:
                return True

            s2_freq[ord(s2[l]) - ord('a')] -= 1
            l += 1

            r += 1
            if r < len(s2):
                s2_freq[ord(s2[r]) - ord('a')] += 1
        
        return False


