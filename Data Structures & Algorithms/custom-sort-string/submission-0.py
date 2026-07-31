class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = []
        for char in order:
            for _ in range(freq.pop(char, 0)):
                res.append(char)
        
        for char, count in freq.items():
            for _ in range(count):
                res.append(char)
        
        return "".join(res)