class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_by = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in group_by:
                group_by[key].append(s)
            else:
                group_by[key] = [s]
        return list(group_by.values())
