class Solution:

    def encode(self, strs: List[str]) -> str:
        delimeter = "#"
        encoded_lst = []
        for s in strs:
            length = len(s)
            encoded_lst.append(str(length) + delimeter + s)
        
        return "".join(encoded_lst)

    def decode(self, s: str) -> List[str]:
        l = 0
        decoded_lst = []
        while l < len(s):
            r = l
            while r < len(s) and s[r] != "#":
                r += 1
            length = int(s[l:r])
            word = s[r + 1: r + 1 + length]
            decoded_lst.append(word)
            l = r + 1 + length
        
        return decoded_lst


