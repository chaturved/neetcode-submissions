class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = { len(s): True}
        def parition(l):
            if l in dp:
                return dp[l]

            for i in range(l, len(s)):
                if s[l:i + 1] in wordDict and parition(i + 1):
                    dp[l] = True
                    return True
            
            dp[l] = False
            return False
        
        return parition(0)

            
            