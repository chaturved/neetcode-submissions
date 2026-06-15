from typing import List

class Solution:
    def find(self, nums, start, end, element):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == element:
                return True
            elif nums[mid] < element:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                if self.find(nums, j + 1, n - 1, target):
                    result.add((nums[i], nums[j], target))

        return [list(triplet) for triplet in result]
