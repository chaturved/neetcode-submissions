class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            prefix[i + 1] = prefix[i] + (1 if word[0] in vowels and word[-1] in vowels else 0)

        result = []
        for start, end in queries:
            result.append(prefix[end + 1] - prefix[start])
        
        return result
            
                
