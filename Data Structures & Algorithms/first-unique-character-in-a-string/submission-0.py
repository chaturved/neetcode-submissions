class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        return -1

