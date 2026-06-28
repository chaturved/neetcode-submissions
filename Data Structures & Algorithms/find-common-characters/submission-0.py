class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_freq = Counter(words[0])

        for word in words[1:]:
            freq = Counter(word)
            for char in common_freq:
                common_freq[char] = min(common_freq[char], freq.get(char, 0))
        
        result = []
        for char, count in common_freq.items():
             result.extend([char] * count)
             
        return result