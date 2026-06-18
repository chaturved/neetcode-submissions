class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq = {}
        window_freq = {}
        for i in range(len(t)):
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1
            window_freq[s[i]] = window_freq.get(s[i], 0) + 1

        matches = 0
        for char, count in t_freq.items():
            if window_freq.get(char, 0) >= count:
                matches += 1

        required = len(t_freq)

        l, r = 0, len(t) - 1
        best_l, best_r = 0, 0
        best_len = float('inf')
        while r < len(s):
            if matches == required:
                if r - l + 1 < best_len:
                    best_l, best_r = l, r
                    best_len = r - l + 1

                c = s[l]
                if window_freq[c] >= t_freq.get(c, 0):
                    matches -= 1
                window_freq[c] -= 1
                if window_freq[c] >= t_freq.get(c, 0):
                    matches += 1
                l += 1
            else:
                r += 1
                if r >= len(s):
                    break
                c = s[r]
                if window_freq.get(c, 0) >= t_freq.get(c, 0):
                    matches -= 1
                window_freq[c] = window_freq.get(c, 0) + 1
                if window_freq[c] >= t_freq.get(c, 0):
                    matches += 1

        if best_len == float('inf'):
            return ""

        return s[best_l: best_r + 1]