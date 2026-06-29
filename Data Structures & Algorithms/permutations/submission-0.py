class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2, 3]
        [2, 1, 3]
        [3, 1, 2]
        """
        result = []
        def backtrack(perm, visited):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                perm.append(nums[i])
                backtrack(perm, visited)
                visited.remove(nums[i])
                perm.pop()
        
        backtrack([], set())
        return result