class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_lst = []
        for s in strs:
            str_lst = [str(len(s)), "_", s]
            encoded_str = "".join(str_lst)
            encoded_lst.append(encoded_str)
        return "".join(encoded_lst)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            length_lst = []
            j = i
            while j < len(s) and s[j] != "_":
                length_lst.append(s[j])
                j += 1
            str_length = "".join(length_lst)
            length = int(str_length)
            j += 1
            strs.append(s[j : j + length])
            i = j + length

        return strs

