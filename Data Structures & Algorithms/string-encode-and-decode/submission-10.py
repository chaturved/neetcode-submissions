class Solution:
    separator = "$"

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            for char in s:
                if char == self.separator:
                    parts.append(self.separator + char)
                else:
                    parts.append(char)
            parts.append(self.separator)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded = []
        word_parts = []
        j = 0
        n = len(s)

        while j < n:
            if s[j] != self.separator:
                word_parts.append(s[j])
            else:
                if j + 1 < n and s[j + 1] == self.separator:
                    word_parts.append(self.separator)
                    j += 1
                else:
                    decoded.append("".join(word_parts))
                    word_parts = []
            j += 1

        return decoded
