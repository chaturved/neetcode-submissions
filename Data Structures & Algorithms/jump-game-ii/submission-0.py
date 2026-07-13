class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        farthest = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
                i += 1
            l = r + 1
            r = farthest
            steps += 1
        
        return steps
        