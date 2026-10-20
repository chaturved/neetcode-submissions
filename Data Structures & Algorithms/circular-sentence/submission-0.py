class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        i = 0
        while i < len(words) - 1:
            if words[i][-1] != words[i + 1][0]:
                return False
            i += 1
        
        return words[0][0] == words[-1][-1]
