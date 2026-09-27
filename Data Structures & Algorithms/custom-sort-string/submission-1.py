class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        str_lst = []
        for char in order:
            if char not in freq:
                continue

            for _ in range(freq[char]):
                str_lst.append(char)
            
            freq.pop(char)
        
        for char, count in freq.items():
            for _ in range(count):
                str_lst.append(char)
        
        return "".join(str_lst)
            