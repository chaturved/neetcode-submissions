class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l, r = 0, 0
        maxFreq = 0
        longest = 0
        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(s[r]) - ord('A')])

            while r - l + 1 - maxFreq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest