class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq_chars = Counter(chars)
        total = 0
        for word in words:
            freq_word = Counter(word)
            flag = False
            for key, value in freq_word.items():
                if key not in freq_chars or value > freq_chars[key]:
                    flag = True
                    break
            if flag:
                continue
            
            total += len(word)
        

        return total