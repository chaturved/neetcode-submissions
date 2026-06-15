class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encode = str(length) + "#" + word
            encoded += encode

        return encoded
        """
        4#neet4#code4#love4#you
        """

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            word_length = ""
            while s[i] != "#" and i < len(s):
                word_length += s[i]
                i += 1

            word_length = int(word_length)
            word = s[i + 1 : i + 1 + word_length]
            result.append(word)
            i = i + 1 + word_length
        
        return result



