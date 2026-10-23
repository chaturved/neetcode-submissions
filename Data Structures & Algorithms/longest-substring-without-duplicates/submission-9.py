class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_window = set()
        l, r = 0, 0
        longest_substring = 0
        while r < len(s):
            while r < len(s) and s[r] not in seen_window:
                seen_window.add(s[r])
                r += 1
            
            longest_substring = max(longest_substring, r - l)

            if r == len(s):
                break

            while l < len(s) and s[r] in seen_window:
                seen_window.remove(s[l])
                l += 1
        
        return longest_substring