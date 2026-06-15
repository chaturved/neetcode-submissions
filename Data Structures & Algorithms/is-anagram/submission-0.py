class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}
        for char_s, char_t in zip(s, t):
            s_count[char_s] = s_count.get(char_s, 0) + 1
            t_count[char_t] = t_count.get(char_t, 0) + 1

        if len(s_count) != len(t_count):
            return False
        
        for char_s in s_count:
            if char_s not in t_count:
                return False
            if s_count[char_s] != t_count[char_s]:
                return False
                
        return True
