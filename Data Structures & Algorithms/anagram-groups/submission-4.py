class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_words = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            freq_words[key].append(s)
        
        return list(freq_words.values())
            