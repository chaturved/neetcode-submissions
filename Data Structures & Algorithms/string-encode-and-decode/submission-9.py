class Solution:
    seperator = "$"

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            i = 0
            while i < len(s):
                if s[i] == self.seperator:
                    encoded += self.seperator + s[i]
                else:
                    encoded += s[i]
                i += 1
            encoded += self.seperator
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        length = len(s)
        word = ""
        j = 0
        while j < len(s):
            if s[j] != self.seperator:
                word += s[j]
            else: # s[j] == self.seperator
                if j + 1 < length and s[j + 1] == self.seperator:
                    word += s[j]
                    j += 1
                else:
                    decoded.append(word)
                    word = ""
            print(j, word)
            j += 1
        return decoded

