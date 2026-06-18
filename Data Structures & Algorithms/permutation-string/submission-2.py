class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1

        l, r = 0, len(s1) - 1
        while r < len(s2):
            if matches == 26:
                return True

            index = ord(s2[l]) - ord('a')
            if s1_freq[index] == s2_freq[index]:
                matches -= 1
            s2_freq[index] -= 1
            if s1_freq[index] == s2_freq[index]:
                matches += 1
            l += 1

            r += 1
            if r >= len(s2):
                break
            index = ord(s2[r]) - ord('a')
            if s1_freq[index] == s2_freq[index]:
                matches -= 1
            s2_freq[index] += 1
            if s1_freq[index] == s2_freq[index]:
                matches += 1

        return False