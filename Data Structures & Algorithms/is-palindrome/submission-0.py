class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        lst = []
        for c in s:
            if c.isalnum():
                lst.append(c.lower())
        t = "".join(lst)
        print(t)

        i, j = 0, len(t) - 1
        while i < j:
            if t[i] != t[j]:
                return False
            i += 1
            j -= 1

        return True