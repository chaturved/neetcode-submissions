class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_seen = set()
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            if s[r] not in window_seen:
                window_seen.add(s[r])
                r += 1
                max_length = max(max_length, r - l)
            else:
                window_seen.remove(s[l])
                l += 1

        return max_length