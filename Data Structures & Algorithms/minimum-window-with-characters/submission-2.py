class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1
        required = len(t_freq)

        window_freq = {}
        matches = 0

        best_l, best_r, best_len = 0, 0, float('inf')
        l = 0
        for r, ch in enumerate(s):
            window_freq[ch] = window_freq.get(ch, 0) + 1
            if ch in t_freq and window_freq[ch] == t_freq[ch]:
                matches += 1

            while matches == required:
                if r - l + 1 < best_len:
                    best_l, best_r, best_len = l, r, r - l + 1

                left_ch = s[l]
                if left_ch in t_freq and window_freq[left_ch] == t_freq[left_ch]:
                    matches -= 1
                window_freq[left_ch] -= 1
                l += 1

        return s[best_l:best_r + 1] if best_len != float('inf') else ""