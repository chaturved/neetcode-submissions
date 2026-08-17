class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        word_lst = []
        while l < len(word1) and r < len(word2):
            word_lst.append(word1[l])
            word_lst.append(word2[r])
            l += 1
            r += 1
        
        while l < len(word1):
            word_lst.append(word1[l])
            l += 1
        
        while r < len(word2):
            word_lst.append(word2[r])
            r += 1
        
        return "".join(word_lst)
        