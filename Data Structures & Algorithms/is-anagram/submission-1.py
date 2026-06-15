class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}
        for char_s, char_t in zip(s, t):
            s_count[char_s] = s_count.get(char_s, 0) + 1
            t_count[char_t] = t_count.get(char_t, 0) + 1

        return s_count == t_count
