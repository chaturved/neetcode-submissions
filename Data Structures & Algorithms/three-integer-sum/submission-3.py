class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        length = len(nums)
        results = []
        for k in range(length - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            left, right = k + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target - nums[k]:
                    results.append([nums[left], nums[right], nums[k]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target - nums[k]:
                    left += 1
                else:
                    right -= 1
        
        return results