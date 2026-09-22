class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, r = 0, 0
        while r < len(abbr):
            if abbr[r].isalpha():
                if l >= len(word) or abbr[r] != word[l]:
                    return False
                l += 1
                r += 1
            else:
                if abbr[r] == '0':
                    return False
                length_strlst = []
                k = r
                while k < len(abbr) and abbr[k].isdigit():
                    length_strlst.append(abbr[k])
                    k += 1

                length = int("".join(length_strlst))
                if l + length > len(word):
                    return False

                l += length
                r = k

        return l == len(word) and r == len(abbr)