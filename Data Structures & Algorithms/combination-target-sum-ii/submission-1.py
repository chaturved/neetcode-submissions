class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        1, 2, 2, 4, 5, 6, 9
        """
        def backtrack(comb, total, start):
            if total > target:
                return
            
            if total == target:
                result.append(comb[:])
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    i += 1
                    continue
                comb.append(candidates[i])
                backtrack(comb, total + candidates[i], i + 1)
                comb.pop()

        result = []
        candidates.sort()
        backtrack([], 0, 0)
        return result
