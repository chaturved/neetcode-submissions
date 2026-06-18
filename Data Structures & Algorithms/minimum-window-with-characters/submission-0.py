class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        1. if len(s) is smaller than len(t), return empty string right away
        2. maintain frequency count of t and frequency count of current window
        3. keep best_len as infinity initially (so we know nothing's been found yet), along with best_l, best_r
        4. if frequency count of current window satisfies t frequency of chars (each char has count >= t's count), store range if smaller than current best
        5. then decrement the frequency of left pointer char first, then move left pointer forward by 1, and keep checking/shrinking like this while it still satisfies t
        6. if it doesn't satisfy t, increment right pointer and update frequency by adding the new char
        7. keep doing this till right pointer reaches end of s
        8. at the end return substring based on best_l and best_r, or empty string if best_len is still infinity
        """
        
        if len(s) < len(t):
            return ""

        t_freq = {}
        window_freq = {}
        for i in range(len(t)):
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1
            window_freq[s[i]] = window_freq.get(s[i], 0) + 1
        
        l, r = 0, len(t) - 1
        best_l, best_r = 0, 0
        best_len = float('inf')
        while r < len(s):
            if all(window_freq.get(char, 0) >= count for char, count in t_freq.items()):
                if r - l + 1 < best_len:
                    best_l, best_r = l, r
                    best_len = r - l + 1
                window_freq[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r >= len(s):
                    break
                window_freq[s[r]] = window_freq.get(s[r], 0) + 1

        if best_len == float('inf'):
            return ""

        return s[best_l: best_r + 1]

                
        
