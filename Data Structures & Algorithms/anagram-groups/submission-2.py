class Solution:
    def count_char(self, s):
        count_s = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        return count_s

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_count = {}
        for s in strs:
            if s in str_count:
                str_count[s] = (str_count[s][0], str_count[s][1] + 1)
            else:
                str_count[s] = (self.count_char(s), 1)
                
        grouped_by_count = {}
        for key, value in str_count.items():
            frozen_value = frozenset(value[0].items())
            if frozen_value in grouped_by_count:
                grouped_by_count[frozen_value].extend([key] * value[1])
            else:
                grouped_by_count[frozen_value] = [key] * value[1]

        return list(grouped_by_count.values())
