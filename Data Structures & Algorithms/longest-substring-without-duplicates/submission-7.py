class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_window = set()
        l, r, max_longest = 0, 0, 0
        
        while r < len(s):
            while r < len(s) and s[r] not in seen_window:
                seen_window.add(s[r])
                r += 1

            max_longest = max(max_longest, r - l)

            if r < len(s):
                while s[l] != s[r]:
                    seen_window.remove(s[l])
                    l += 1
                seen_window.remove(s[r])
                l += 1

        return max_longest