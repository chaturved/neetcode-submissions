class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        odd_seen = False
        for char, count in freq.items():
            length += count - (count % 2)
            if count % 2:
                odd_seen = True
        
        return length + 1 if odd_seen else length

            

            
            