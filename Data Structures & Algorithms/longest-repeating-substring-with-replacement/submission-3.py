class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l, r = 0, 0
        res, max_freq = 0, 0
        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            r += 1
            
            while r - l - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l)

        return res

