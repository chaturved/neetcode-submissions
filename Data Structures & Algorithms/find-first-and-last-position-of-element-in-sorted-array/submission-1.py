class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left_boundary():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        def find_right_boundary():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l

        if not nums:
            return [-1, -1]

        lo = find_left_boundary()
        if nums[lo] != target:
            return [-1, -1]

        hi = find_right_boundary()
        if nums[hi] == target:
            return [lo, hi]
            
        return [lo, hi - 1]