class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        result = []
        for start, end in queries:
            count = 0
            for i in range(start, end + 1):
                word = words[i]
                if len(word) == 1:
                    count += 1 if word[0] in vowels else 0
                elif word[0] in vowels and word[-1] in vowels:
                    count += 1
            result.append(count)
        return result
                
