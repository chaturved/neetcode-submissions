class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, r = 0, 0
        max_freq = 0
        longest = 0
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])

            while r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest