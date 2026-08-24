class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}
        for i, char in enumerate(s):
            min_idx, max_idx = char_index.get(char, (i, i))
            char_index[char] = min(min_idx, i), max(max_idx, i)
        

        max_length = -1
        for min_idx, max_idx in char_index.values():
            max_length = max(max_length, max_idx - min_idx - 1) 
        
        return max_length

