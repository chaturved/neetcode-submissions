class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []
        for s in strs:
            str_value = ["0"] * 256
            for i, char in enumerate(s):
                str_value[i] = str(ord(char))
            encoded_str = "_".join(str_value)
            encoded_strs.append(encoded_str)
        return " ".join(encoded_strs)



    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
            
        lst = []
        for encoded_str in s.split(" "):
            str_lst = []
            for value in encoded_str.split("_"):
                if value == "0":
                    continue
                char = chr(int(value))
                str_lst.append(char)
            decoded_str = "".join(str_lst)
            lst.append(decoded_str)
        return lst

                