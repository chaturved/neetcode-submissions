class Solution:
    def longestPalindrome(self, s: str) -> str:
        resstart, reslen = 0, 0

        for i in range(len(s)):
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    resstart = l
                    reslen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    resstart = l
                    reslen = r - l + 1
                l -= 1
                r += 1
        

        return s[resstart : resstart + reslen]
