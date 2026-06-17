class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        left, right = 0, 0
        seen = set()
        while right < len(s):
            if s[right] in seen:
                longest_length = max(longest_length, right - left)
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                right += 1
        
        return max(longest_length, right - left)