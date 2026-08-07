class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_freq_list(s):
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            return freq
        
        return get_freq_list(s) == get_freq_list(t)